import os
from nltk.tag import StanfordNERTagger
from nltk.corpus import stopwords
from incidents import arr
import string

st = StanfordNERTagger('english.conll.4class.distsim.crf.ser.gz')

def get_location(text):
	loc = ""
	text = text.translate(None, string.punctuation)
	tags = st.tag(text.split())
	for tag in tags:
		if(tag[1] == u'LOCATION' or tag[1] == u'ORGANIZATION' or tag[1] == u'PERSON'):
			loc += tag[0]
			loc += " "
	return loc

def filter_stopwords(text):
	stop = set(stopwords.words('english'))
	return [i for i in text.split() if i not in stop]

def get_reason(text):
	rsn = ""
	text = text.translate(None, string.punctuation)
	for word in text.split():
		if word in arr:
			rsn += str(word)
			rsn += " "
	return rsn

def main():
	for line in open("/home/nehal/Desktop/traffic_samr/tweets.txt"):
		print "TEXT: "+str(line).replace("\n","")
		print "AFTER REMOVING STOPWORDS: "+str(filter_stopwords(line))
		print "LOCATION: "+str(get_location(line))
		print "REASON: "+str(get_reason(line))
		print "\n"

if __name__ == '__main__':
	main()
