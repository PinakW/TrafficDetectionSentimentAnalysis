import matplotlib.pyplot as plt

count = 0
actual = []
expected = []
total = 63

for line in open("/home/nehal/Desktop/traffic_samr/output123.csv"):
	csv_row = line.split()
	actual.append(str(csv_row[0]).rsplit(",", 1)[1])
	#print actual
actual = actual[1:]

for line in open("/home/nehal/Desktop/traffic_samr/samr/data/test_sentiment.txt"):
	expected.append(line.replace("\n",""))

for pos,i in enumerate(actual):
	print(expected[pos] + " " + i)
	if expected[pos] == i:
		count = count + 1;

labels = 'Correct','Incorrect'
colors = ['green', 'red']
sizes = [count,63-count]
explode = (0.1, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()
