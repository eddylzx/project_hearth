import spacy
from spacy import displacy
import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Test texts for NLP
textA = "One of my patients died. Today I had 40 patients assigned to me, compared to yesterday’s 20. For each patient I spent an average of maybe 4 hours with, and they were all on ventilators, which we need more of. I also went through 2 masks today, I don’t know whether I will have enough to last through the week"
textB = "I was given a mask today by a kid. I was assigned 40 patients today, 20 more than yesterday. I slept for 2 hours and worked from 19 hours. However 1 guy recovered today. 2 people passed away. I have been using the same mask for 2 weeks, and I only have 1 mask left. I am experiencing some symptons including coughing and sore throat, but I don't have time to rest."
textC = "Covid-19 ourbreak is unstoppable and threatening our life everyday. my mental health is at a 5. I would rate my physical health as 8. I do not have enough masks and 4 patients of mine passed-away this morning."
textD = "61 people passed away today. I am very tired, I want to sleep. I only slept for 1 hour last night."
textE = "60 people passed away today."
textWordMap = 'I really care about all my patients. However one of my favorite patients was transfered to another hospital. The rest of my patients feel unsafe. Some patients have been experiencing worsened symptoms. All the patients in my hostpial need more resources. If my patients run out of resources, we will face sever death toll. On March 19 i threw up, and I can feel and the stress is real. My colleagues have been feeling stressed out too. We barely have time to talk to each other about our stress. stress, masks, masks, masks, masks, masks, masks, masks, masks, ventilator, ventilator, ventilator, ventilator, support, support, sleep, sleep, sleep, sleep, sleep, sleep, sleep, sleep, eat, symptoms, symptoms, symptoms. '

diarytext = None

nlp = None
text = None

master_dict = {}  # key: list of data points

# for list of units that not to include in the noun count dictionary
unit_noun_list = ["a.m", "p.m", "yesterday", "today", "second", "minute", "day", "hour", "week", "month", "year"] 


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
#     list_of_verbs = [token for token in text if token.pos_ == "VERB"]
#     return list_of_verbs

def extract_noun_verb():
    global text
    global master_dict
    
    from spacy.lang.en.stop_words import STOP_WORDS

    for token in text:
        # if token.is_stop == False and len(token) > 3 and \
        #     token.lemma_ != 'yesterday' and token.lemma_ != 'today':
        #     filtered_sentence.append(token.lemma_)
                
        if token.pos_ == 'NOUN' and token.is_stop == False and len(token) > 3:
            if token.dep_ != 'DATE' and token.dep_ != 'CARDINAL' and token.dep_ != 'QUANTITY' and\
                token.lemma_ not in unit_noun_list:
                
                if token.lemma_ in master_dict:
                    master_dict[token.lemma_] += 1
                else:
                    master_dict[token.lemma_] = 1
    print(master_dict)
    # gen_wordcloud(master_dict)
    # tocsv()

# helper function to export to csv file
def tocsv(master_dict):
    with open('datapoints_noun_count_pairs.csv', mode='w') as wfile:
        for key in master_dict.keys():
            wfile.write("%s, %s\n" % (key, master_dict[key]))

# def read_txt():
#     global diarytext
#     f = open('diary2.txt', 'r')
#     diarytext = f.read()
#     # print(diarytext)
#     return diarytext

# def gen_wordcloud(master_dict):
#     wordcloud = WordCloud(background_color='white',
#                         width=1500,
#                         height=1000
#                         ).generate_from_frequencies(master_dict)
#     # use .generate(space_separated_string) - to generate cloud from text

#     plt.figure(figsize=(9,6))
#     plt.imshow(wordcloud)
#     plt.axis('off')
#     plt.show()

# To view tree, go to: http://localhost:5000/
def display_tree():
    global text
    displacy.serve(text, style="dep")

if __name__ == '__main__':
    setup(textA)
    extract_noun_verb()
    #display_tree()