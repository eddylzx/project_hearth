import csv
import re


text = 'Today I had 20 patients assigned to me, compared to yesterday’s 20. For each patient I spent an average of maybe 4 hours with, and they were all on ventilators, which we need more of. I also went through 2 masks today, I don’t know whether I will have enough to last through the week.'

datapoints = ['patients', 'masks', 'gloves', 'scrubs', 'face shields', 'ventilators', 'hours',
			'washed my hand']


def get_noun_count_pair(text):
	dict_data = dict()
	sent_list = sent_tokenize(text)
	for sent in sent_list:
		split_sent = sent.split()
		items_count = re.findall(r'\d+', sent)
		for datapoint in datapoints:
			if datapoint in sent:
				if datapoint in dict_data:
					dict_data[datapoint].append(items_count)
				else:
					dict_data[datapoint] = items_count
					
	print(dict_data)


def sent_tokenize(text):
    sentences = re.split(r"[.,!?]", text)
    sentences = [sent.strip(" ") for sent in sentences]
    return sentences[:-1]


if __name__ == "__main__":
	get_noun_count_pair(text)



