import os
import numpy as np
import pandas as pd

article = pd.read_csv(".\\one_hot_encoding.csv", encoding = 'cp1252')
article.pop('Unnamed: 0')
article.to_csv('one_hot_encoding.txt', sep = ' ', header=False)