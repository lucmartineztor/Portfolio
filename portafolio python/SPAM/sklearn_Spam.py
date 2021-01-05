from nltk.corpus import words
import numpy as np
import pandas as pd
import joblib
import string
from nltk.corpus import stopwords
import nltk
from time import time
from sklearn.pipeline import Pipeline
import io
import requests
import pickle


df = pd.read_csv("spam.csv" )# encoding="utf-8")
print(df.head(10))
print(df.describe())
df.groupby('Label').describe()
df['spam']=df['Label'].apply(lambda x: 1 if x=='spam' else 0)
df.head()

def process_text(text):
    Punctuation=''.join([char for char in text if char not in string.punctuation])
    Punctuation=nltk.tokenize.word_tokenize(Punctuation)
    #clean_words=[word for word in Punctuation.split() if word.lower() not in stopwords.words('spanish', 'english')]
    clean_words=[word for word in Punctuation if word.lower() not in stopwords.words('spanish', 'english')]
    return clean_words
df['EmailText'].head().apply(process_text)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(df.EmailText,df.spam, test_size=0.15)

from sklearn.feature_extraction.text import CountVectorizer
v=CountVectorizer(analyzer=process_text)
X_trainCount=v.fit_transform(X_train.values)
X_testCount=v.transform(X_test)
print(X_trainCount)

pickle.dump(X_train,open("X__Train","wb"))

print("------------------------Naive Bayes------------------------------")

from sklearn.naive_bayes import MultinomialNB
model=MultinomialNB()
model.fit(X_trainCount,y_train)

InitialTime=time()
for email in df['EmailText'].head(10):

    emailsCount=v.transform([email])
    model.predict(emailsCount)
    model.score(X_testCount, y_test)
  
    print(model.predict(emailsCount))
    if model.predict(emailsCount)==[1]:
        print (email, "is spam")
EndingTime=time()
Totaltime=EndingTime - InitialTime
print('tiempo de ejecución total: ',Totaltime)
print('tiempo de ejecución promedio: ',(int(Totaltime))/10)


email= input("Texto: ")
emailsCount=v.transform([email])
model.predict(emailsCount)
#model.score(X_testCount, y_test)
print(model.predict(emailsCount))

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

pred=model.predict(X_testCount)
print("prediccion: " )
print(model.predict(X_testCount))
print("valores de y: " , y_test.values)
print("Reporte de clasificación : ")
print(classification_report(y_test,pred))
print("Matriz pp, pf, fp,ff: ")
print(confusion_matrix(y_test,pred))
print("Porcentaje de ajuste")
print( accuracy_score(y_test,pred))

#Guardar el codigo

Model=model.fit(X_trainCount,y_train)
joblib.dump(Model, "modelSaved")

#Lectura de codigo
#loadMOdel=joblib.load("modelSaved")
#print(loadMOdel.score(X_testCount, y_test))


# with open("modeleSaved",'rb') as f:
#   np=pickle.load(f)
#   print(np.score(x_test, y_test))

# print("------------------------SVC-----------------------------")

# from sklearn.svm import SVC
# model=SVC()
# model.fit(X_trainCount,y_train)

# emailsCount=v.transform([emails])
# model.predict(emailsCount)
# X_testCount=v.transform(X_test)
# model.score(X_testCount, y_test)

# clf =Pipeline([
#     ('vectorizer',CountVectorizer()),
#     ('scv', SVC())
# ])
# print(clf.fit(X_train, y_train))
# print(clf.score(X_test, y_test))
# print(clf.predict([emails]))


# print("---------------------------Decision tree classifier-----------------------")

# from sklearn.tree import DecisionTreeClassifier
# model=DecisionTreeClassifier()
# model.fit(X_trainCount,y_train)

# emailsCount=v.transform([emails])
# model.predict(emailsCount)
# X_testCount=v.transform(X_test)
# model.score(X_testCount, y_test)

# clf =Pipeline([
#     ('vectorizer',CountVectorizer()),
#     ('DTC',DecisionTreeClassifier())
# ])
# print(clf.fit(X_train, y_train))
# print(clf.score(X_test, y_test))
# print(clf.predict([emails]))

# print("---------------------------K Neighbors Classifier-----------------------")

# from sklearn.neighbors import KNeighborsClassifier
# model=KNeighborsClassifier()
# model.fit(X_trainCount,y_train)

# emailsCount=v.transform([emails])
# model.predict(emailsCount)
# X_testCount=v.transform(X_test)
# model.score(X_testCount, y_test)

# clf =Pipeline([
#     ('vectorizer',CountVectorizer()),
#     ('KNC', KNeighborsClassifier())
# ])
# print(clf.fit(X_train, y_train))
# print(clf.score(X_test, y_test))
# print(clf.predict([emails]))


# print("--------------------------- Logistic Regression-----------------------")
# from sklearn.linear_model import LogisticRegression
# model=LogisticRegression()
# model.fit(X_trainCount,y_train)

# emailsCount=v.transform([emails])
# model.predict(emailsCount)
# X_testCount=v.transform(X_test)
# model.score(X_testCount, y_test)

# clf =Pipeline([
#     ('vectorizer',CountVectorizer()),
#     ('LR', LogisticRegression())
# ])
# print(clf.fit(X_train, y_train))
# print(clf.score(X_test, y_test))
# print(clf.predict([emails]))

# print("--------------------------- Random Forest -----------------------")



# #Aplica el modelo estadistico
# InitialTime= time()
# from sklearn.ensemble import RandomForestClassifier
# model=RandomForestClassifier()
# model.fit(X_trainCount, y_train)

# # Predice si es spam o no un ejemplo de correo que digite el usuario desde consola

# emailsCount=v.transform([emails])
# model.predict(emailsCount)
# model.score(X_testCount, y_test)

# from sklearn.pipeline import Pipeline
# clf =Pipeline([
#     ('vectorizer',CountVectorizer()),
#     ('RandomForestClassifier', RandomForestClassifier())
# ])

# print("ajuste: ",clf.fit(X_train, y_train))
# print("puntaje: ",clf.score(X_test, y_test))
# print("clasificación: ",model.predict(emailsCount))

# EndingTime = time()
# print('tiempo de ejecución : ',EndingTime - InitialTime)


# #Analisis de prediccion de correos en la base de datos (solamente)


# pred=model.predict(X_testCount)
# print("prediccion: " , model.predict(X_testCount))
# print("valores de y: " , y_test.values)
# print("Reporte de clasificación : ", classification_report(y_test,pred))
# print("Matriz pp, ff, fp pf: ", confusion_matrix(y_test,pred))
# print("Porcentaje de ajuste",accuracy_score(y_test,pred))

# #Guardar y leer modelo

# #joblib.dump(model, "modelSaved")
# #loadModel=joblib.load("modelSaved")
# #print(loadModel.score(X_testCount, y_test))

# print("--------------------------- Ensemble -----------------------")