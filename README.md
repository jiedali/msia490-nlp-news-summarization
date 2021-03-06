# **News Headline Generation**

MSiA 490 Text Analytics Project

Jieda Li

November 2020 



## **Goal**: 
* My goal of this project is to build a news headline generator exploring both abstractive and extractive text summarization technique.

## **Approach**: 

### **Method 1: Abstractive Model**: 
* Encoder-Decoder model, bi-directional LSTM with Attention for Encoder, basic unidirectional LSTM for decoder.

### **Method 2: Extractive Model**: 
* Use pre-trained BERT to create sentence embeddings, then perform K-means clustering on the sentence embeddings, choose the sentence(s) closest to the center of cluster centroid as the summary.

### **Method3: Extractive Model**: 
* TextRank, a graph-based approach similar to PageRank based on similarity-weighted link between each pair of sentences

## **Experiments and Results**:

* Detailed experimentation results can be found at /deliverables/msia490_nlp_project_paper.pdf

## Directory structure 

```
├── README.md                         <- You are here
├── requirements.txt                  <- Python package dependencies 
├── app/                              <- contains Dockerfile for running the app using Docker Container
│   - Dockerfile
├── data/                             <- Folder that contains data used for generating the summary
│
├── deliverables/                     <- Paper write-up and Presentation slides 
│
├── results/                          <- Results generated including summaries from the abstractive model, validation results of abstractive model, training curve

```
## Instructions on running the dockerized application

Follow instructions below to run the app using docker container and generate a summary of your own choice of news article!

Go to root directoy
```bash
 cd msia490-nlp-news-summarization
``` 

Run following command to build docker image
```bash
 docker build -f app/Dockerfile -t new_sum .
``` 

Run following command to run a docker container and launch the API
```bash
 docker run new_sum python3 api.py
``` 

Now you will be able to view the app at: http://127.0.0.1:5000/apidocs/

#### Here is the screen shot of the swagger documentation interface:

![alt text](https://github.com/jiedali/msia490-nlp-news-summarization/blob/main/figures/swagger_interface.png)

You can click "try it out" and input your raw text string in the field of "text", upon click "execute" you will be able to see the summary generated by the extractive method.



## Instructions on How to Run the app (without using Docker)
Alternatively, you can do following steps to run the app without using Docker

#### After download the repo, first install the required packages

```bash
 pip install -r requirements.txt
```
#### Go to the root directory

```bash
 cd msia490-nlp-news-summarization
``` 

#### Run following command to launch the app

```bash
 python api.py
``` 

#### Now You should be able to access the api at your local host: http://127.0.0.1:5000/apidocs/

## Instructions on generating summary with the Encoder-Decoder Model

The training, evaluation and summary prediction using the encoder-decoder Model is done on Google Colab via Jupyter notebook.
Follow steps below to generate summary output using the model

* Open the jupyter notebook abstractive_lstm_run2_predict_evaluate.ipynb via Google colab
* Download the required glove embeddings from following URL: https://nlp.stanford.edu/data/wordvecs/glove.42B.300d.zip
* Save the extracted file to following mounted google drive location (so the runtime can access it)
```bash
 /content/gdrive/MyDrive/glove/glove.42B.300d.txt
``` 
* Download the trained model from my Google Drive Link:
* https://drive.google.com/drive/folders/1-HrqUphcxMT-Ti2Ra4EO_3Elztcz_3rm?usp=sharing
, save it here:
```bash
 /content/gdrive/MyDrive/saved_model/
``` 
* Save the news article you wish to summarize as a text file and name it valid.article.filter.test.txt, save it here:
```bash
 /content/gdrive/MyDrive/sumdata/train/valid.article.filter.test.txt
``` 
You can rename the text file, but if you change the name, you also need to change the file path in the code.

* run the following cell to generate summary prediction using my trained model object:
```
import tensorflow as tf
tf.reset_default_graph()

class args:
    pass
  
args.num_hidden=150
args.num_layers=2
args.beam_width=10
args.glove="store_true"
args.embedding_size=300

args.learning_rate=1e-3
args.batch_size=64
args.num_epochs=10
args.keep_prob = 0.8
args.toy=True

args.with_model="store_true"

valid_article_path = default_path + "sumdata/train/valid.article.filter.test.txt"

print("Loading dictionary...")
word_dict, reversed_dict, article_max_len, summary_max_len = build_dict("valid", args.toy)
print("Loading validation dataset...")
valid_x = build_dataset("valid", word_dict, article_max_len, summary_max_len, args.toy)
valid_x_len = [len([y for y in x if y != 0]) for x in valid_x]
print("Loading article and reference...")
article = get_text_list(valid_article_path, args.toy)
reference = get_text_list(valid_title_path, args.toy)

with tf.Session() as sess:
    print("Loading saved model...")
    model = Model(reversed_dict, article_max_len, summary_max_len, args, forward_only=True)
    saver = tf.train.Saver(tf.global_variables())
    ckpt = tf.train.get_checkpoint_state(default_path + "saved_model/")
    saver.restore(sess, ckpt.model_checkpoint_path)

    batches = batch_iter(valid_x, [0] * len(valid_x), args.batch_size, 1)

    print("Writing summaries to 'result.txt'...")
    for batch_x, _ in batches:
        batch_x_len = [len([y for y in x if y != 0]) for x in batch_x]

        valid_feed_dict = {
            model.batch_size: len(batch_x),
            model.X: batch_x,
            model.X_len: batch_x_len,
        }

        prediction = sess.run(model.prediction, feed_dict=valid_feed_dict)
        prediction_output = [[reversed_dict[y] for y in x] for x in prediction[:, 0, :]]
        print(prediction_output)
        summary_array = []
        with open(default_path + "result.txt", "a") as f:
            for line in prediction_output:
                summary = list()
                for word in line:
                    if word == "</s>":
                        break
                    if word not in summary:
                        summary.append(word)
                summary_array.append(" ".join(summary))
                print(" ".join(summary), file=f)

    print('Summaries have been generated')
``` 
* Generated summary will be stored in a separate text file called result.txt, under:

```bash
 /content/gdrive/MyDrive/result.txt
``` 
## References

Following repos/code are referenced for this project:
* Lecture7.zip example code
* https://github.com/dongjun-Lee/text-summarization-tensorflow
* https://github.com/DeepsMoseli/Bidirectiona-LSTM-for-text-summarization-
* https://github.com/dmmiller612/bert-extractive-summarizer

