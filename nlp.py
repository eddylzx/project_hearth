# MIT COVID-19 Hackathon
# Marcus Chu, Charles Tung Fang, Shih Bobin
# 4/3/2020
# The goal of this NLP one (as opposed to Josh's hard coded one) is that we won't know what we're looking for
# so by identifying nouns and logging them into a dict, we can just keep expanding data categories 

# Run this before you use this: 
# pip install spacy
# python3 -m spacy download en_core_web_sm

#TODO:
# - Implement noun count pairs (via nummod dependencies) (DONE)
# - Add datapoint to master dict (DONE)
# - Add temporal considerations to data points (yesterday, today etc.)
# - Figure out what other data we can add
# - Export data to .csv or something so that Alay can use it (DONE)
# - Browse spacy examples 

import spacy
from spacy import displacy
import csv

nlp = None
text = None

master_dict = {} #key: list of data points

def setup(input_text):
    global nlp, text
    nlp = spacy.load("en_core_web_sm")
    text = nlp(input_text)

# def get_nouns():
#     global text
#     list_of_nouns = [chunk.text for chunk in text.noun_chunks]
#     print("Noun phrases:", list_of_nouns)
#     return list_of_nouns

# def get_verbs():
#     global text
#     list_of_verbs = [token.lemma_ for token in text if token.pos_ == "VERB"]
#     print("Verbs:", list_of_verbs)
#     return list_of_verbs

# Get the noun count pairs using a hybrid of spaCy's nummod and NLP
def get_noun_count_pairs():
    global text 
    global master_dict
    noun_count_dict = {}
    
    # the verb of the current sentence
    cur_verb = ""
    # init key val variables
    dict_key = ""
    dict_val = ""
    
    # Using nummod dependency
    for token in text:
        # keep track of the verb of the current sentence
        if token.pos_ == "VERB":
            cur_verb = token.text
            
        # Reset key and value when reaching the end of a sentence 
        # token is a conjuction or the start of a sentence -> renew dictionary key & value
        if token.pos_ == "CCONJ" or token.sent_start:
            dict_key = ""
            dict_val = ""
        
        # Basic nummond operation to update key and val
        if token.dep_ == "nummod":
            dict_key = token.head.text
            dict_val = token

        # append to noun count dictionary at the end of the sentence or middle of a sentence seperated by conjunction    
        if token.text == '.' or token.pos_ == 'CCONJ':
            # make key descriptive by adding current verb to the key
            if '_' not in dict_key:
                dict_key = cur_verb + "_" + dict_key
            
            if dict_key in noun_count_dict and dict_val:
                noun_count_dict[dict_key].append(dict_val)
            elif dict_val:
                noun_count_dict[dict_key] = [dict_val]
            
            # renew noun count key and value after each append to the noun count dictionary 
            dict_key = "" 
            dict_val = ""
        
    print("Nummod:", noun_count_dict)

    # export to csv file
    tocsv(noun_count_dict)
    
    return noun_count_dict

# helper function to export to csv file
def tocsv(master_dict):
    with open ('datapoints_noun_count_pairs.csv', mode = 'w') as wfile:
        for key in master_dict.keys():
            wfile.write("%s, %s\n" % (key, master_dict[key]))
    

# To view tree, go to: http://localhost:5000/
def display_tree():
    global text
    displacy.serve(text, style="dep")
