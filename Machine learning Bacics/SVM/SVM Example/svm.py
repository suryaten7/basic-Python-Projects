# -*- coding: utf-8 -*-
"""SVM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z2AQ4w2YTFv8oFCfq_cHSO0mSDAX2b5J
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

from sklearn.datasets import load_breast_cancer

cancer=load_breast_cancer()

cancer.keys()

df_feat=pd.DataFrame(cancer["data"],columns=cancer["feature_names"])

df_feat.head()

df_feat.info()

df_feat.describe()

from sklearn.model_selection import train_test_split

X=df_feat
y=cancer["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

from sklearn.svm import SVC

model=SVC()

model.fit(X_train,y_train)

predictions=model.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix

confusion_matrix(y_test,predictions)

print(classification_report(y_test,predictions))

"""#suppose class 0 not working properly your model need to have it parameter adjusted.
#use GridSearchCV it will find right parameter for your model
"""

from sklearn.model_selection import GridSearchCV

param_grid={"C":[0.1,1,10,100,1000],
            "gamma":[1,0.1,0.01,0.001,0.0001]}

grid=GridSearchCV(SVC(),param_grid,verbose=3)

grid.fit(X_train,y_train)

#grab best parameter
grid.best_params_

#grab best estimator
grid.best_estimator_

grid_predict=grid.predict(X_test)

print(confusion_matrix(y_test,grid_predict))

print(classification_report(y_test,grid_predict))

