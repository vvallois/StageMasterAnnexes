import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.stats import lognorm
import scipy.stats

#Génération d'une distribution suivant la loi lognormal
sigmabis, scale = 0.942646, 2.433333333
mubis = np.log(scale)
sample = np.random.lognormal(np.log(2.8432803665655411), 0.29731261148742899, size=1501)*1000
counts, bins, ignored = plt.hist(sample, 100, range=[0, 20000], normed=False, align='mid', color='r', alpha=0.6, label="Lognormal")

#Récupération du DataSet
data = csv.reader(open('transactions-per-second.csv', 'rb'), delimiter=",", quotechar='|')
column2 = []
for row in data:
    column2.append(row[1])
n = np.array(column2).astype(np.float32)*1000
counts, bins, ignored = plt.hist(n, 100, range=[0, 20000], normed=False, align='mid', color='g', alpha=0.6, label="Dataset")
plt.legend(loc='upper right')
plt.show()