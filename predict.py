from text_rank import text_rank_summarize
from helpers import process_input



def summarize(text):
	"""returns the top 1 sentence from the summary"""
	result = text_rank_summarize(text,num_sentences=1)

	return result

# usually we will import from predict in the api.py, to run predictions
# can also run the predict standalone and produce summary using the files in the data folder

if __name__ =="__main__":

	text = process_input('./data/example_file.txt')
	result = text_rank_summarize(text, num_sentences=1)
	print("The generated summary is:")
	print(result)