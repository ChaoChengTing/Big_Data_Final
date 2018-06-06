import sklearn
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from lib.statistic.cluster.utils import load_vector
from lib.statistic.dim_reduction import dimension_reduction
from lib.statistic.noise import sklearn_LocalOutlierFactor
import numpy as np

words, X = load_vector(".\\TSNE_vector.txt", verbose=True)
km = KMeans(n_clusters=39)
y_pred = km.fit_predict(X)
plt.figure(figsize=(10, 6))
plt.xlabel('Salary')
plt.ylabel('Rate of working')
plt.scatter(X[:, 0], X[:, 1], c=y_pred) #C是第三維度 已顏色做維度
plt.show()
km.cluster_centers_