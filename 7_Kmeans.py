import sklearn
from sklearn.cluster import KMeans, MeanShift, estimate_bandwidth
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from lib.statistic.cluster.utils import load_vector
from lib.statistic.dim_reduction import dimension_reduction
from lib.statistic.noise import sklearn_LocalOutlierFactor
import numpy as np

words, X = load_vector(".\\TSNE_vector.txt", verbose=True)
now = 0
for clusterNum in range(2,40):    
    km = KMeans(n_clusters=int(clusterNum), random_state=10)
    x_pred = km.fit_predict(X)
    tmp = silhouette_score(X,x_pred,metric='euclidean')
    print('clusterNum = '+ str(clusterNum) + '\tsilhouette_score =', tmp)
    if tmp >= now:
        now = tmp
        num = clusterNum

km = KMeans(n_clusters=num, random_state=10)
x_pred = km.fit_predict(X)
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=x_pred, s=10, cmap='viridis')
centers = km.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=100, alpha=0.8)
plt.show()