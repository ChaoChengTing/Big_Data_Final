import pandas as pd
from functools import reduce
import os
article = pd.read_csv(".\\CleanArticle.csv", encoding = 'cp1252')
articleData = pd.DataFrame(article)
comment = pd.read_csv(".\\CleanComment.csv", encoding = 'cp850')
comment.pop('commentBody')
comment.pop('newDesk')
comment.pop('typeOfMaterial')
comment['recommendations']=comment['recommendations'].astype('int64')
commentData = pd.DataFrame(comment)
# 計算每一篇文章recommendations數量
print ("-1")
recommendationsData = commentData.groupby('articleID')[["recommendations"]].sum()
# 計算每一篇文章有多少comments
print ("-2")
commentData = commentData.groupby('articleID').count()
commentData["recommendations"] = recommendationsData
print (commentData)
# articleData = articleData['typeOfMaterial'].unique()
# articleData = articleData['typeOfMaterial'].unique()
# for i in range(len(articleData)):
#     print(articleData[i])
frames = [articleData, commentData]
# print (frames)
df_final = reduce(lambda left,right: pd.merge(left,right,on='articleID'), frames)
# print (df_final)
df_final.to_csv('merge.csv')
os.system("pause")
