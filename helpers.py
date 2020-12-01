import matplotlib.pyplot as plt

def process_input(raw_input_path):
	with open(raw_input_path, "r") as myfile:
	# with open("data/example3.txt", "r") as myfile:
		data = myfile.read().replace('\n', '')

	return data

def plot():
	"""helper function to plot the training curve"""
	a=[60.79889, 58.90382, 53.8132, 50.03202, 54.350708, 51.79844, 51.27045, 52.818398, 54.42515, 48.845245, 44.2248, 48.558258, 40.96916, 34.270683, 33.418537, 40.13305, 39.486263, 38.337467, 44.896057, 36.90664, 38.79937, 40.222206, 37.5149, 37.736073, 37.196064, 35.048428, 42.131306, 41.650036, 31.583973, 35.46926, 31.577965, 27.100735, 33.8819]
	plt.figure()
	plt.plot(range(len(a)),a)
	plt.savefig('./figures/lstm_attention_training.png')