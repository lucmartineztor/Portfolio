# KERAS

import pandas as pd
import numpy as np
import tensorflow as tf
import keras
from sklearn import preprocessing
from keras.models import Model
from keras.layers import LSTM, Lambda, Activation, Dense, Dropout, Input, Embedding
from sklearn.model_selection import train_test_split
import string
from nltk.corpus import stopwords
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping
from keras.preprocessing import sequence
from keras.optimizers import RMSprop
from time import time
from sklearn.metrics import confusion_matrix, classification_report
from collections import Counter
import os
from keras.models import model_from_json
from keras.models import Sequential
import pickle
import nltk

from dominio import dominio1

nltk.download('stopwords')

data=pd.read_csv('spam.csv')




stop=stopwords.words ("english")+stopwords.words ("spanish")

def remove_stopwords(EmailText):
	EmailText=[word.lower() for word in EmailText.split() if word.lower() not in stop]
	return " ".join(EmailText)

data["EmailText"]=data["EmailText"].map(remove_stopwords)
print(data["EmailText"])

y=data['Label']
x=data['EmailText']
print (y)

def counter_word(EmailText):
	count = Counter()
	for i in EmailText.values:
		for word in i.split():
			count[word] += 1
	return count

EmailText = data.EmailText

counter=counter_word(EmailText)
print(len(counter))
max_words= len(counter)

le=preprocessing.LabelEncoder()
y=le.fit_transform(y)
y=y.reshape(-1,1)
spam_value=y[0]
ham_value=y[2]
print(spam_value, ham_value)
pickle.dump(spam_value,open("spam_value","wb"))
pickle.dump(ham_value,open("ham_value","wb"))
print(y)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)
pickle.dump(x_train,open("x_train"+dominio1,"wb"))


# num_classes = max(y_train) + 1
# print(': {}'.format(num_classes))

#max_words = 3800
max_len=30

tok=Tokenizer(num_words=max_words, filters='¡¿!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True)
print(tok.fit_on_texts(x_train))
sequences=tok.texts_to_sequences(x_train)
sequences_matrix=sequence.pad_sequences(sequences,maxlen=max_len)


model=Sequential()
model.add(Embedding(max_words, 50, input_length=max_len))
model.add(LSTM(64))
model.add(Dense(256, name= 'FC1'))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1, name= 'out_layer'))
model.add(Activation('sigmoid'))
model.summary()

#Entrenamiento
model.compile(loss='binary_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])
print(model.metrics_names)
model.fit(sequences_matrix, y_train, batch_size=128, epochs =10, validation_split=0.2, callbacks=[EarlyStopping(monitor='val_loss', min_delta=0.0001)])
model.save(dominio1)
test_sequences=tok.texts_to_sequences(x_test)
test_sequences_matrix=sequence.pad_sequences(test_sequences,maxlen=max_len)
accr=model.evaluate(test_sequences_matrix, y_test)
print('Test set\n Loss:{:0.3f}\n Accuracy: {:0.3f}'.format(accr[0],accr[1]))

pred=model.predict(test_sequences_matrix)
print("pred: ",type(pred))


preds=list(map(lambda x:1 if float(x)>0.5 else 0, pred))

print("confusion matrix")
print(confusion_matrix(y_test,preds))
print("classification report")
print(classification_report(y_test, preds))

# InitialTime=time()
# for email in data['EmailText'].head(10):
#     emailsCount=tok.texts_to_sequences([email])
#     emailsCount=sequence.pad_sequences(emailsCount,maxlen=max_len)
#     model.predict(emailsCount)
#     #model.score(X_testCount, y_test)

#     print(model.predict(emailsCount))
#     if model.predict(emailsCount)>[0.5]:
#         print (email, "is spam")
# EndingTime=time()
# Totaltime=EndingTime - InitialTime
# print('tiempo de ejecución total: ',Totaltime)
# print('tiempo de ejecución promedio: ',(int(Totaltime))/100)

# x=0
# while x<=1:
# 	testing_context=input('Email por clasificar: ')
# 	testing_context= remove_stopwords(testing_context)
# 	txts=tok.texts_to_sequences([testing_context])
# 	txts=sequence.pad_sequences(txts, maxlen=max_len)
# 	preds=model.predict(txts)
# 	print(preds)
# 	x=x+1
testing_context=input('Email por clasificar: ')
testing_context= remove_stopwords(testing_context)
txts=tok.texts_to_sequences([testing_context])
txts=sequence.pad_sequences(txts, maxlen=max_len)
preds=model.predict(txts)
print(preds)

model.save(dominio1)
MODEL_DIR = '/home/desarrollo/Documentos/python/'+dominio1+"/1"
tf.keras.models.save_model(
    model,
    MODEL_DIR,
	overwrite=True,
    include_optimizer=True,
    save_format=None,
    signatures=None,
    options=None
)

print("---------- adam ------------------")

sequences_matrix=sequence.pad_sequences(sequences,maxlen=max_len)
max_len=60
model=Sequential()
model.add(Embedding(max_words, 50, input_length=max_len))
model.add(LSTM(64))
model.add(Dense(256, name= 'FC1'))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1, name= 'out_layer'))
model.add(Activation('sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()
print(model.metrics_names)





model.fit(sequences_matrix, y_train, batch_size=128, epochs =10, validation_split=0.2, callbacks=[EarlyStopping(monitor='val_loss', min_delta=0.0001)])
test_sequences=tok.texts_to_sequences(x_test)
test_sequences_matrix=sequence.pad_sequences(test_sequences,maxlen=max_len)
""" model.save("network2.h5") """
accr=model.evaluate(test_sequences_matrix, y_test)
print('Test set\n Loss:{:0.3f}\n Accuracy: {:0.3f}'.format(accr[0],accr[1]))

from sklearn.metrics import confusion_matrix
pred=model.predict(test_sequences_matrix)
preds=list(map(lambda x:1 if float(x)>0.5 else 0, pred))

print("confusion matrix")
print(confusion_matrix(y_test,preds))
print("classification report")
print(classification_report(y_test, preds))



# x=0
# while x<=1:
# 	testing_context=input('Email por clasificar: ')
# 	testing_context= remove_stopwords(testing_context)
# 	txts=tok.texts_to_sequences([testing_context])
# 	txts=sequence.pad_sequences(txts, maxlen=max_len)
# 	preds=model.predict(txts)
# 	print(preds)
# 	x=x+1

# for email in data['EmailText'].head(10):
# 	testing_context= remove_stopwords(email)
# 	txts=tok.texts_to_sequences([testing_context])
# 	txts=sequence.pad_sequences(txts, maxlen=max_len)
# 	preds=model.predict(txts)
# 	if preds>0.5:
# 		print(email, "is spam")
# model_json = model.to_json()
# with open("model.json", "w") as json_file:
#     json_file.write(model_json)

# model.save_weights("model2.h5")
# print("Saved model to disk")


pickle.dump(max_words,open("max_words","wb"))
print("max_words")



