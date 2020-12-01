# **News Headline Generation**

MSiA 490 Text Analytics Project

Jieda Li

November 2020 



### **Goal**: 
* My goal of this project is to build a news headline generator exploring both abstractive and extractive text summarization technique.

### **Approach**: 

##### **Method 1 Abstractive Model**: 
* Encoder-Decoder model, bi-directional LSTM with Attention for Encoder, basic unidirectional LSTM for decoder.

##### **Method 2: Extractive Model**: 
* Use pre-trained BERT to create sentence embeddings, then perform K-means clustering on the sentence embeddings, choose the sentence(s) closest to the center of cluster centroid as the summary.

##### **Method3: Extractive Model**: 
* TextRank, a graph-based approach similar to PageRank based on similarity-weighted link between each pair of sentences

### **Experiments and Results**:

* Detailed experimentation results can be found at /deliverables/msia490_nlp_project_paper.pdf

## Directory structure 

```
├── README.md                         <- You are here
├── requirements.txt                  <- Python package dependencies 
├── api                               <- script to runs the REST app  
│
├── data                              <- Folder that contains data used for generating the summary
│
├── deliverables/                     <- Paper write-up and Presentation slides 
│
├── figures/                          <- Generated figures for paper and slides                             <- Source code
│
├── results/                          <- Results generated including summaries from the abstractive model, validation results of abstractive model, training curve

```

## Instructions on How to Run the app

Follow instructions below to run the app and generate a summary of your own news article!

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

#### Here is the screen shot of the swagger documentation interface:



## Instructions on running the dockerized application

