import pandas as pd

final = pd.read_csv(".\\merge.csv")
DF = pd.DataFrame(final)
commentDF = DF.groupby('newDesk').comment.count().to_frame()
commentSumDF = DF.groupby('newDesk').comment.sum().to_frame()
recommendationsSumDF = DF.groupby('newDesk').recommendations.sum().to_frame()
newDF = commentDF.join(commentSumDF, lsuffix='_has_comment', rsuffix='_comment_num')
finalDF = newDF.join(recommendationsSumDF)
print(finalDF)
finalDF.to_csv('conclusion.csv')