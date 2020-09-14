import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics
import joblib
import os
dataframe=pd.read_csv("images.csv")
dataframe=dataframe.sample(frac=1).reset_index(drop=True)
#print(dataframe)
X=dataframe.drop(['2'],axis=1)
Y=dataframe['2']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20)
model = SVC(kernel='linear')
model.fit(X_train, Y_train)
#os.mkdir("SVM")
joblib.dump(model,open("SVM.sav","wb"))
loadedmodel=joblib.load("SVM.sav")
pred=loadedmodel.predict(X_test)
print(metrics.accuracy_score(Y_test,pred))

