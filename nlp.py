# MIT COVID-19 Hackathon
# Marcus Chu, Charles Tung Fang
# 4/3/2020

import spacy
from spacy import displacy

# Text is the string produced by the speech-to-text functions
nlp = spacy.load("en_core_web_sm")
text = nlp(input_text)

def get_nouns():
	list_of_nouns = [chunk.text for chunk in doc.noun_chunks]
	print("Noun phrases:", list_of_nouns)
	return list_of_nouns

def get_verbs():
	list_of_verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
	print("Verbs:", list_of_verbs)
	return list_of_verbs

def get_noun_count_pairs():
	pass

def display_tree():
	displacy.serve(text, style="dep")

if __name__ == "__main__":
	pass

