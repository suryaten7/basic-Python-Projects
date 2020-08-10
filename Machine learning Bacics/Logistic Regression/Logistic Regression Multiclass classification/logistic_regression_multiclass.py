# -*- coding: utf-8 -*-
"""logistic_regression_multiclass.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jy1Lsh5iKW__xvpaysu7FmI6x5zCNDwB

<h2 style='color:blue' align="center">Logistic Regression: Multiclass Classification</h2>

In this tutorial we will see how to use logistic regression for multiclass classification.
"""

# Commented out IPython magic to ensure Python compatibility.
from sklearn.datasets import load_digits
# %matplotlib inline
import matplotlib.pyplot as plt
digits = load_digits()

plt.gray() 
for i in range(5):
    plt.matshow(digits.images[i])

dir(digits)

digits.data[0]

"""<h4 style='color:purple'>Create and train logistic regression model</h4>"""

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(digits.data,digits.target, test_size=0.2)

len(X_train)

len(X_test)

model.fit(X_train, y_train)

"""<h4 style='color:purple'>Measure accuracy of our model</h4>"""

model.score(X_test, y_test)

model.predict(digits.data[0:5])

"""<h4 style='color:purple'>Confusion Matrix</h4>"""

y_predicted = model.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predicted)
cm

import seaborn as sn
plt.figure(figsize = (10,7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')