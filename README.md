# **News Headline Generation**

MSiA 490 Text Analytics Project

Created by Jieda Li

November 2020 



### **Goal**: 
My goal of this project is to build a news headline generator exploaring both abstractive and extractive text summarization technique.

### **Approach**: 

**Method 1 Abstractive Model**: Encoder-Decoder based, bi-directional LSTM with Attention for Encoder, basic unidirectional LSTM for decoder.

**Method 2: Extractive Model**: Use pre-trained BERT to create sentence embeddings, then perform K-means clustering on the sentence embeddings, choose the sentence that is closest ot eh center of each cluster centroid as the summary. Use can specify how many sentences they would like to be in the summary.

**Method3: Extractive Model**: TextRank

### **Experimentation**:

Detailed experimentation results can be found at /deliverables/msia490_nlp_project_paper.pdf
 

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
├── figures/                          <- Generated figures for paper and slides
│
├── models/                           <- BERT model used for generate the sentence embeddings
│
├── src/                              <- Source code
│

```

## Instructions on How to Run

Follow instructions below to run the app and generate a summary of your own news article!


