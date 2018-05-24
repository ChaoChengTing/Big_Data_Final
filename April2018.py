#import the pandas library and aliasing as pd
import pandas as pd
import os
article = pd.read_csv("D:\\Big Data\\ArticlesApril2018.csv", encoding = 'cp1252')
# df.pop('columnID') #刪除該行
# print (article)
# print (article['newDesk'])
# s = pd.Series(list(article))
# print(pd.get_dummies(s))
# 轉換成dataframe
articleData = pd.DataFrame(article)
# 將multimedia非數字的列轉換成NaN
articleData['multimedia'] = articleData['multimedia'].convert_objects(convert_numeric=True)
# multimedia中的任意列如為NaN 則將整列刪除
articleData = articleData.dropna()
print(articleData)
# 輸出
# articleData.to_csv('CleanArticle.csv')
comment = pd.read_csv("D:\\Big Data\\CommentsApril2018.csv", encoding = 'cp850')
commentData = pd.DataFrame(comment)
commentData['recommendations'] = commentData['recommendations'].convert_objects(convert_numeric=True)
commentData = commentData.dropna()
commentData.to_csv('CleanComment.csv')
os.system("pause")
