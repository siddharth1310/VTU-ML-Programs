from sklearn import datasets
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()


x = iris.data
y = iris.target

print(x)
print(y)
xtrain, xtest, ytrain, ytest = train_test_split(x, y)

model1 = KMeans(n_clusters=3)
model1.fit(xtrain, ytrain)
xpred1 = model1.predict(xtest)
print(model1.score)

print('Accuracy Score From KMeans ->')
print(accuracy_score(xpred1, ytest))

model2 = GaussianMixture(n_components=3)
model2.fit(xtrain, ytrain)
xpred2 = model2.predict(xtest)
print(model2.score)

print('Accuracy Score From Gaussian Mixture ->')
print(accuracy_score(xpred2, ytest))
