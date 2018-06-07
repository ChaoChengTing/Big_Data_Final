import sklearn
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from lib.statistic.cluster.utils import load_vector
from lib.statistic.dim_reduction import dimension_reduction
from lib.statistic.noise import sklearn_LocalOutlierFactor
import numpy as np

words, X = load_vector(".\\noise_removed_vectors.txt", verbose=True)

X_2d = dimension_reduction(X, reduction_method='sklearn_TSNE', verbose=True, **dict({'n_components':3}))
with open('TSNE_vector.txt', 'w') as f:
	for row in X_2d:
		line = ' '.join(map(str, row)) + '\n'
		f.write(line)
