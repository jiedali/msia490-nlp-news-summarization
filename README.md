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
├── app                               <- contains Dockerfile for running the app using Docker Container
│
├── data                              <- Folder that contains data used for generating the summary
│
├── deliverables/                     <- Paper write-up and Presentation slides 
│
├── figures/                          <- Generated figures for paper and slides                             <- Source code
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





