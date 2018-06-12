import sklearn
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

#noise
noise_pred = sklearn_LocalOutlierFactor(X, verbose=True, **dict({'contamination': 0.2}))
plt.figure(figsize=(12,8))
plt.scatter(X_2d[noise_pred!=-1][:,0], X_2d[noise_pred!=-1][:,1], marker='o',s=3,c='blue')
plt.title('Visualization - noise removal ratio {}'.format(0.2))
plt.savefig('visual_tsne_noise_removal2.png')
plt.scatter(X_2d[noise_pred==-1][:,0], X_2d[noise_pred==-1][:,1], marker='o',s=3,c='black')
plt.savefig('visual_tsne_noise_removal1.png')

with open('noise_removed_vectors_test.txt', 'w') as f:
    for w, v, label in zip(words, X, noise_pred):
        if label != -1:
            line = w + ' ' + ' '.join(map(str, v)) + '\n'
            _ = f.write(line)