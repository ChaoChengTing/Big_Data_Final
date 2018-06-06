import pandas as pd

article = pd.read_csv(".\\merge.csv", encoding = 'cp1252')
article.columns = ['Number', 'Number2', 'articleID', 'newDesk', 'typeOfMaterial', 'comment', 'recommendations']
article.pop('Number')
article.pop('Number2')
recommend_edge = [0, 1000, 3000, 5000, 10000, 100000]
recommend_name = ['0-1000', '1000-3000', '3000-5000', '5000-10000', '10000up']
article['recommendationsGroup'] = pd.cut(article['recommendations'], recommend_edge, labels = recommend_name, include_lowest=True)
article.pop('recommendations')
article = pd.get_dummies(article)
print (article)
article.to_csv('one_hot_encoding.csv')