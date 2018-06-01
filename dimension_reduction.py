import matplotlib.pyplot as plt
from lib.statistic.cluster.utils import load_vector
from lib.statistic.dim_reduction import dimension_reduction
from lib.statistic.noise import sklearn_LocalOutlierFactor

# read
words, X = load_vector(".\\one_hot_encoding.txt", verbose=True)

# 降成二維
X_2d = dimension_reduction(X, reduction_method='sklearn_TSNE', verbose=True, **dict({'n_components':2}))

# tsne figure
plt.figure(figsize=(12,8))
plt.scatter(X_2d[:,0], X_2d[:,1], marker='o', s=3, c='blue')
plt.title('Visualization - {} data'.format(len(X_2d)))
plt.savefig('visual_tsne.png')