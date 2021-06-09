from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

iris = datasets.load_iris()

x = iris.data
y = iris.target

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(xtrain, ytrain)
xpred = classifier.predict(xtest)

print('Classification Accuracy -', classifier.score(xtest, ytest))
print('Confusion Matrix')
print(confusion_matrix(xpred, ytest))
print('Accuracy Metrics')
print(classification_report(xpred, ytest))
