# MIT COVID-19 Hackathon
# Marcus Chu, Charles Tung Fang
# 4/3/2020
# The goal of this NLP one (as opposed to Josh's hard coded one) is that we won't know what we're looking for
# so by identifying nouns and logging them into a dict, we can just keep expanding data categories 

# Run this before you use this: 
# pip install spacy
# python3 -m spacy download en_core_web_sm

#TODO:
# - Implement noun count pairs (via nummod dependencies)
# - Add datapoint to master dict
# - Add temporal considerations to data points (yesterday, today etc.)
# - Figure out what other data we can add
# - Export data to .csv or something so that Alay can use it
# - Browse spacy examples

import spacy
from spacy import displacy

nlp = None
text = None

master_dict = {} #key: list of data points

def setup(input_text):
    global nlp, text
    nlp = spacy.load("en_core_web_sm")
    text = nlp(input_text)

def get_nouns():
    global text
    list_of_nouns = [chunk.text for chunk in text.noun_chunks]
    print("Noun phrases:", list_of_nouns)
    return list_of_nouns

def get_verbs():
    global text
    list_of_verbs = [token.lemma_ for token in text if token.pos_ == "VERB"]
    print("Verbs:", list_of_verbs)
    return list_of_verbs

def get_noun_count_pairs():
    # 1 case - Look for nummod dependencies
    # Add data point to master_dict
    pass

# To view tree, go to: http://localhost:5000/
def display_tree():
    global text
    displacy.serve(text, style="dep")

if __name__ == "__main__":
    setup("Today I had 20 patients assigned to me, compared to yesterday’s 20. For each patient I spent an average of maybe 4 hours with, and they were all on ventilators, which we need more of. I also went through 2 masks today, I don’t know whether I will have enough to last through the week")
    display_tree()
