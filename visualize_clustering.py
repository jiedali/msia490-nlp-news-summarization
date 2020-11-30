# this is a helper script to visualize the sentence clustering results
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# first get the embeddings
from summarizer import Summarizer
model = Summarizer()
with open ("data/example3.txt", "r") as myfile:
    data=myfile.read().replace('\n','')

result_all_sentences = model.run_embeddings(data,num_sentences=7)

pca=PCA(n_components=2)
pca.fit(result_all_sentences)

result = model.run_embeddings(data,num_sentences=1)

# Get embeddings for all sentences
# result is the 4*N embedding matrix
# do PCA on the result matrix and get PCA scores



# project each of the sentence embedding onto the 2 principle components
score = np.dot(result,pca.components_.transpose())

# Plot the 3 summary sentences, x-axis is 1st principal component, y-axis is the 2n principal component
plt.figure()
# Get embeddings for all sentences

# project each of the sentence embedding onto the same 2 PC
score_all_sent = np.dot(result_all_sentences,pca.components_.transpose())
plt.figure()
plt.scatter(score_all_sent[0:8,0],score_all_sent[0:8,1],s=100,color='b')
plt.scatter(score[0:2,0],score[0:2,1],s=150,color='r')
plt.savefig('./figures/debug_2.png')
