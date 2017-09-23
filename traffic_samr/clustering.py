import json
from nltk.corpus import stopwords
from nltk.tag import StanfordNERTagger
from extract import get_location
from extract import filter_stopwords
import string

st = StanfordNERTagger('english.conll.4class.distsim.crf.ser.gz')

data = dict()
keys = []

def cluster(text):
	text = text.translate(None, string.punctuation)
	text = str(filter_stopwords(text))
	location = get_location(text)
	text1 = ""
	for word in text.replace("[","").replace("]","").replace("'","").replace(",","").split():
		text1 += word
		text1 += " "
	if str(location) in data:
		data[str(location)].append(text1)
	else:
		data[str(location)] = [text1]
	return data

def main():
	for line in open("/home/nehal/Desktop/traffic_samr/clusterdata.txt"):
		json_data = json.dumps(cluster(line))
	print json_data

if __name__ == '__main__':
	main()

#cluster("Heavy traffic near Matunga Flyover due to flooding")
