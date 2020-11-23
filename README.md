# **News Summarization**

MSiA 490 Text Analytics Project

Created by Jieda Li

November 2020 



### **Goal**: 
My goal of this project is to build a news summarizer that facilitate efficient news reading.

### **Approach**: 
My main approach is perform extractive summary by using a pre-trained BERT model to create sentence embedding, then perform K-means clustering on the sentence embeddings and finally select the sentence that is closest to the center of each cluster centroid as the summary sentence.

By specifying the number of clusters, user can pick how many sentences they want to have in the final summary. 

### **Experimentation**:
I have experimented with various models on creating embeddings (BERT and GPT-2) and clustering methods (K-means and Gaussian Mixture Models). I also compared the results from this approach to the well-known TextRank method.
 

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
