import os
import numpy as np
import pandas as pd

article = pd.read_csv(".\\one_hot_encoding.csv", encoding = 'cp1252')
article.pop('Unnamed: 0')
idx = np.random.randint(len(article), size=len(article))
selected_X = article.values[idx,:]
print(selected_X.shape)
with open('one_hot_encoding_test.txt', 'w') as f:
	for row in selected_X:
		line = ' '.join(map(str, row)) + '\n'
		f.write(line)