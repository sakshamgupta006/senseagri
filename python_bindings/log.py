import pandas
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold
import numpy as np
from sklearn import cross_validation


titanic = pandas.read_csv("/home/cooper/Downloads/UP-Hapur-Wheat-Price(2006-16)",delim_whitespace=True,header=None)
# Initialize our algorithm
alg = LogisticRegression(random_state=1)
# Compute the accuracy score for all the cross validation folds.  (much simpler than what we did before!)
predictors = [9,10,11]
scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic[8], cv=3)
# Take the mean of the scores (because we have one for each fold)
print(scores.mean())