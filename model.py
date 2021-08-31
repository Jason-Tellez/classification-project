import numpy as np
import pandas as pd
import scipy.stats as stats

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import permutation_importance



def most_imp_feat(clf, df):
    '''
    Function loops list of columns names and random forest feature importance values and returns most valuable features
    '''
    z = []
    x = pd.Series(clf.feature_importances_)
    y = pd.Series(df.columns)
    for i in range(len(x)):
        if x[i] >= .02:
            z.append(y[i])
    return z


def most_imp_knn(X, y):
    '''
    Creates a default KNN classifier and fits it to training data.
    Uses permutation_importance to evaluate permutation importance for feature evaluation.
    Returns list of higher-performing column names.
    '''
    feats = []
    model = KNeighborsClassifier()
    # fit the model
    model.fit(X, y)
    results = permutation_importance(model, X, y, scoring='accuracy')
    # get importance
    importance = results.importances_mean
    # summarize feature importance
    for i,v in enumerate(importance):
        if v > 0.0005:
            feats.append(X.columns[i])
    return feats