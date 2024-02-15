import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
from sklearn import metrics
import csv

cities = []
with open("cities.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|') 
    for row in reader: # each row is a list
        cities.append(row[0])
my_data = genfromtxt('data.csv', delimiter=',')
parties = ["Labor", "Yamina", "United Torah Judaism", "Joint Arab List", "Religious Zionism",
"Blue and White", "Israel Beitenu", "Likud", "Meretz", "United Arab List", "Yesh Atid",
"Shas", "New Hope"]
ranks = my_data[:, 0]
votes = my_data[:, 1:]
for i in range(len(votes)):
    votes[i] = votes[i] / sum(votes[i])
xtx1 = np.linalg.inv(np.matmul(votes.T, votes))
xty = np.matmul(votes.T, ranks)
factors = np.matmul(xtx1, xty)
for i in range(len(factors)):
    print("The factor for ", parties[i], " is ", factors[i])
preds = []
for i in range(len(votes)):
    preds.append(np.dot(factors, votes[i]))
rounds = []
for i in range(len(preds)):
    rounds.append(round(preds[i]))
confusionMatrix = metrics.confusion_matrix(ranks, rounds)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix= confusionMatrix, display_labels= [0,1,2,3,4,5,6,7,8,9,10])
cm_display.plot()
plt.show()
differences = {}
for i in range(len(cities)):
    differences[i] = abs(preds[i] - ranks[i])
iter = 0
for index, diff in sorted(differences.items(), key=lambda p:p[1]):
    if (iter == 0):
        print("10 most accurate predications are:")
    if (iter < 10):
        print(cities[index], ranks[index], preds[index], diff)
    if (iter == len(cities) - 10):
        print("10 least accurate predications are:")
    if (iter >= len(cities) - 10):
        print(cities[index], ranks[index], preds[index], diff)
    iter += 1
