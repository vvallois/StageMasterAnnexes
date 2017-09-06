import matplotlib.pyplot as plt
import scipy
import scipy.stats
import csv
import numpy as np


data = csv.reader(open('transactions-per-second.csv', 'rb'), delimiter=",", quotechar='|')
column2 = []
for row in data:
    column2.append(row[1])
n = np.array(column2).astype(np.float32)*1000

x = scipy.arange(10000)
counts, bins, ignored = plt.hist(n, 100, range=[0, 10000], normed=False, align='mid', color='g', alpha=0.6, label="Dataset")
dist_names = ['gamma', 'beta', 'rayleigh', 'norm', 'pareto', 'lognorm']

for dist_name in dist_names:
    dist = getattr(scipy.stats, dist_name)
    param = dist.fit(n)
    pdf_fitted = dist.pdf(x, *param[:-2], loc=param[-2], scale=param[-1])*170000
    plt.plot(pdf_fitted, alpha=0.6, label=dist_name)
    plt.xlim(0,10000)
plt.legend(loc='upper right')

plt.show()