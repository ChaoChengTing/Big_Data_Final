import pandas as pd
import os
article = pd.read_csv(".\\CleanArticle.csv", encoding = 'cp1252')
articleData = pd.DataFrame(article)
comment = pd.read_csv(".\\CleanComment.csv", encoding = 'cp850')
commentData = pd.DataFrame(comment)
print(commentData)
# articleData = articleData['typeOfMaterial'].unique()
# for i in range(len(articleData)):
#     print(articleData[i])

os.system("pause")
