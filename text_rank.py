import spacy
import pytextrank
from math import sqrt
from operator import itemgetter


def text_rank_summarize(text, num_sentences):
	# example text
	# load a spaCy model, depending on language, scale, etc.
	nlp = spacy.load("en_core_web_sm")

	# add PyTextRank to the spaCy pipeline
	tr = pytextrank.TextRank()
	nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)
	#
	doc = nlp(text)
	# construct a list of the sentence boundaries with a phrase vector
	sent_bounds = [ [s.start, s.end, set([])] for s in doc.sents ]
	limit_phrases = 4

	phrase_id = 0
	unit_vector = []

	# ==================================
	for p in doc._.phrases:
		print(phrase_id, p.text, p.rank)

		unit_vector.append(p.rank)

		for chunk in p.chunks:
			print(" ", chunk.start, chunk.end)

			for sent_start, sent_end, sent_vector in sent_bounds:
				if chunk.start >= sent_start and chunk.start <= sent_end:
					print(" ", sent_start, chunk.start, chunk.end, sent_end)
					sent_vector.add(phrase_id)
					break

		phrase_id += 1

		if phrase_id == limit_phrases:
			break
	# =================================
	# debug: print all the sentence
	# for sent in doc.sents:
	#     print(sent)

	#
	sum_ranks = sum(unit_vector)
	unit_vector = [ rank/sum_ranks for rank in unit_vector ]
	#
	sent_rank = {}
	sent_id = 0

	# Now loop through each sentence, compute the euclidean distance from the unit vector
	for sent_start, sent_end, sent_vector in sent_bounds:
		print(sent_vector)
		sum_sq = 0.0

		for phrase_id in range(len(unit_vector)):
			print(phrase_id, unit_vector[phrase_id])

			if phrase_id not in sent_vector:
				sum_sq += unit_vector[phrase_id] ** 2.0

		sent_rank[sent_id] = sqrt(sum_sq)
		sent_id += 1

	print(sent_rank)

	sorted(sent_rank.items(), key=itemgetter(1))

	limit_sentences = num_sentences

	sent_text = {}
	sent_id = 0

	for sent in doc.sents:
		sent_text[sent_id] = sent.text
		sent_id += 1

	num_sent = 0

	for sent_id, rank in sorted(sent_rank.items(), key=itemgetter(1)):
		print(sent_id, sent_text[sent_id])
		num_sent += 1

		if num_sent == limit_sentences:
			break

	return sent_text[sent_id]