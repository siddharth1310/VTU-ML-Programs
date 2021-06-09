import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score

msg = pd.read_csv('data6.csv', names=['message', 'label'])
msg['labelnum'] = msg.label.map({'pos': 1, 'neg': 0})

X = msg.message
y = msg.labelnum

xtrain, xtest, ytrain, ytest = train_test_split(X, y)

count_vect = CountVectorizer()
xtrain_dtm = count_vect.fit_transform(xtrain)
xtest_dtm = count_vect.transform(xtest)
clf = MultinomialNB().fit(xtrain_dtm, ytrain)
xpred = clf.predict(xtest_dtm)

print('Accuracy metrics')
print('Accuracy of the classifer is', accuracy_score(xpred, ytest))
print('Confusion matrix')
print(confusion_matrix(xpred, ytest))
print('Recall and Precison ')
print(recall_score(xpred, ytest))
print(precision_score(xpred, ytest))
