import pandas as pd
from functools import reduce
import os
article = pd.read_csv(".\\CleanArticle.csv", encoding = 'cp1252')
article.pop('headline')
article.pop('multimedia')
articleData = pd.DataFrame(article)
comment = pd.read_csv(".\\CleanComment.csv", encoding = 'cp850')
comment.pop('commentBody')
comment.pop('newDesk')
comment.pop('typeOfMaterial')
comment['recommendations']=comment['recommendations'].astype('int64')
commentData = pd.DataFrame(comment)
# 計算每一篇文章recommendations數量
recommendationsData = commentData.groupby('articleID')[["recommendations"]].sum()
# 計算每一篇文章有多少comments
commentData = commentData.groupby('articleID').count()
commentData["recommendations"] = recommendationsData
commentData.columns = ['comment', 'recommendations']
print (commentData)
# articleData = articleData['typeOfMaterial'].unique()
# articleData = articleData['typeOfMaterial'].unique()
# for i in range(len(articleData)):
#     print(articleData[i])
# print (frames)
df_final = pd.merge(articleData, commentData, on='articleID', validate="one_to_one")
# print (df_final)
df_final.to_csv('merge.csv')