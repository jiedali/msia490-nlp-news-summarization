from summarizer import Summarizer
from helpers import process_input

model = Summarizer()

def summarize(text):
	"""returns the top 1 sentence from the summary"""
	result = model(text,num_sentences=1)

	return result

# usually we will import from predict in the api.py, to run predictions
# can also run the predict standalone and produce summary using the files in the data folder

if __name__ =="__main__":

	text = process_input('./data/example_file.txt')
	result = model(text, num_sentences=1)
	print("The generated summary is:")
	print(result)