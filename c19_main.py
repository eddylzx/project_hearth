import speech_recognition as SR
import NLP_tmap as parser

# Test texts for NLP
textA = "Today I had 40 patients assigned to me, compared to yesterday’s 20. For each patient I spent an average of maybe 4 hours with, and they were all on ventilators, which we need more of. I also went through 2 masks today, I don’t know whether I will have enough to last through the week"
textB = "I was assigned 40 patients today, 20 more than yesterday. I slept for 2 hours and worked from 19 hours. However 1 guy recovered today. 2 people passed away. I have been using the same mask for 2 weeks, and I only have 1 mask left. I am experiencing some symptons including coughing and sore throat, but I don't have time to rest."
textC = "Coivd-19 ourbreak is unstoppable and threatening our life everyday. my mental health is at a 5. I would rate my physical health as 8. I do not have enough masks and 4 patients of mine passed-away this morning."
textD = "61 people passed away today. I am very tired, I want to sleep. I only slept for 1 hour last night."

# # NLP
# nlp.setup(textA)
# # display_tree()
# nlp.get_noun_count_pairs()
# # NLP
def nlp_parser(text):
    parser.setup(text)
    # parser.display_tree()
    parser.extract_noun_verb()


# Speech to text
recognizer = SR.Recognizer()
with SR.Microphone() as source:
    print("Speak:")
    audio = recognizer.listen(source)

try:
    print("You said: " + recognizer.recognize_google(audio))
    nlp_parser(recognizer.recognize_google(audio))
except SR.UnknownValueError:
    print("Could not understand audio")
except SR.RequestError as e:
    print("Could not request results; {0}".format(e))

