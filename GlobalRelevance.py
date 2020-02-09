import spacy
from geotext import GeoText
from nltk import word_tokenize
from nltk.util import ngrams
from textblob import TextBlob


def getscores(headline):
    headline_sent = TextBlob(headline)
    objectivity = 1-headline_sent.sentiment.subjectivity - abs(headline_sent.sentiment.polarity)*0.1
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(headline)
    countries = [i[0] for i in GeoText(headline).country_mentions.items()]
    relevance = 0
    relevant = False
    political = ["pm","election","poll","prime minister","president","minister","trade","bank of"]
    violence = ["riot","protest","violence","march","rampage", "mass shooting","ceasefire","governor","troop","clash","ethnic","nationalist"]
    for ent in doc.ents:
        if ent.label_ == "GPE" or ent.label_ == "NORP":
            # print(ent.text)
            relevant = True

    token = word_tokenize(headline)
    bigram = list(ngrams(token, 2))

    for eachgram in bigram:
        if eachgram in political or eachgram in violence:
            # print(eachgram)
            relevance += 0.1

    for eachgram in bigram:
        if eachgram in violence:
            # print(eachgram)
            relevance += 0.5

    for word in headline.split():
            if word in political:
                relevance += 0.02

    for word in headline.split():
            if word in violence:
                relevance += 0.01

    return countries, relevant, relevance, objectivity




# print(getscores("American dies of coronavirus in Shanghai; five Britons infected in French Alps"))
#([], False, 0.01)
