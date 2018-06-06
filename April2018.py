#import the pandas library and aliasing as pd
import pandas as pd
from random import randint
import os
article = pd.read_csv(".\\ArticlesApril2018.csv", encoding = 'cp1252')
# 轉換成dataframe
articleData = pd.DataFrame(article)
# 將multimedia非數字的列轉換成NaN
articleData['multimedia'] = articleData['multimedia'].convert_objects(convert_numeric=True)
# multimedia中的任意列如為NaN 則將整列刪除
articleData = articleData.dropna()
print(articleData)
# 輸出
articleData.to_csv('CleanArticle.csv')
comment = pd.read_csv(".\\CommentsApril2018.csv", encoding = 'cp850')
commentData = pd.DataFrame(comment)
print(type(commentData['recommendations'][0]))
commentData['recommendations'] = commentData['recommendations'].convert_objects(convert_numeric=True)
commentData = commentData.dropna()
commentData = commentData.query('recommendations < 1000')
print(commentData)
commentData.to_csv('CleanComment.csv')
os.system("pause")
