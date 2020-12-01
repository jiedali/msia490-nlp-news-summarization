import argparse
from helpers import process_input
from summarizer import Summarizer
from text_rank import text_rank_summarize


# this script will take an input news article
if __name__ =="__main__":

	"""wrapper function to run summary prediction with different models"""
	parser = argparse.ArgumentParser(description="pass the raw text you wanted to summarize")

	parser.add_argument('--preprocess', help='indicate if this is for preprocessing only', default=True)
	parser.add_argument('--path', help='input raw text path', default='./data/example_file.txt')
	parser.add_argument('--numsent', help='number of sentences desired in the final summary', default=1)
	args = parser.parse_args()

	# first process input text into string
	data = process_input(args.path)


	# produce results from method 2: extractive method with k-means
	model_1 = Summarizer()
	summary_1 = model_1(data,num_sentences=args.numsent)
	print("Summary from extracitve model 1 is:")
	print(summary_1)

	# produce results from method 3: TextRank
	summary_2 = text_rank_summarize(text=data,num_sentences=args.numsent)
	print("summary from TextRank model is:")
	print(summary_2)


