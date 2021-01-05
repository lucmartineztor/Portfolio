# A PARTIR DE LOS MODELOS GUARDADOS

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
import os
from keras.models import Sequential
import pickle
import nltk
import joblib
import tempfile
from keras.models import load_model
from sklearn.feature_extraction.text import CountVectorizer


df = pd.read_csv("spam.csv" )
stop= stopwords.words ("english")+stopwords.words ("spanish")

def remove_stopwords(EmailText):
    EmailText=[word.lower() for word in EmailText.split() if word.lower() not in stop]
    return " ".join(EmailText)

def process_text(text):
    Punctuation=''.join([char for char in text if char not in string.punctuation])
    Punctuation=nltk.tokenize.word_tokenize(Punctuation)
    #clean_words=[word for word in Punctuation.split() if word.lower() not in stopwords.words('spanish', 'english')]
    clean_words=[word for word in Punctuation if word.lower() not in stop]
    return clean_words

max_len=30

max_words= pickle.load(open("max_words","rb"))
print(max_words)
x_train=pickle.load(open("x_train","rb"))
print(x_train)
X_train=pickle.load(open("X__Train","rb"))
print(X_train)

tok=Tokenizer(num_words=max_words, filters='¡¿!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True)
tok.fit_on_texts(x_train)
sequences=tok.texts_to_sequences(x_train)
sequences_matrix=sequence.pad_sequences(sequences, maxlen=max_len)



v=CountVectorizer(analyzer=process_text)
X_trainCount=v.fit_transform(X_train.values)


model=load_model('network1.h5')
model1=load_model('network2.h5')
model2=joblib.load("modelSaved")

# i=0 
# while i<=2:
# 	testing_context=input('Email por clasificar: ')
# 	testing_contexts= remove_stopwords(testing_context)
# 	txts=tok.texts_to_sequences([testing_contexts])
# 	txts=sequence.pad_sequences(txts, maxlen=60)
# 	emailsCount=v.transform([testing_context])
# 	pred=model.predict(txts)
# 	preds=model1.predict(txts)
# 	Preds=model2.predict(emailsCount)
# 	print(testing_context)
# 	print("Deep Learning-RMSprop: ",pred)
# 	print("Deep Learning-adam: ",preds)
# 	print("Learning Machine-Naive Bayes",Preds)
# 	i=i+1




# InitialTime=time()
# for email in df['EmailText'].head(10):
# 	testing_contexts= remove_stopwords(email)
# 	emailsCount=v.transform([email])
# 	txts=tok.texts_to_sequences([testing_contexts])
# 	txts=sequence.pad_sequences(txts, maxlen=60)
# 	pred=model.predict(txts)
# 	preds=model1.predict(txts)
# 	Preds=model2.predict(emailsCount)
# 	print("Deep Learning-RMSprop: ",pred)
# 	print("Deep Learning-adam: ",preds)
# 	print("Learning Machine-Naive Bayes",Preds)
# 	if model2.predict(emailsCount)==[1] and model1.predict(txts)>0.5 and model.predict(txts)>0.5:
# 		print (email, "is spam")
# EndingTime=time()
# Totaltime=EndingTime - InitialTime
# print('tiempo de ejecución total: ',Totaltime)
# print('tiempo de ejecución promedio: ',(int(Totaltime))/10)



MODEL_DIR = tempfile.gettempdir()
version = 1
export_path = os.path.join(MODEL_DIR, str(version))
print('export_path = {}\n'.format(export_path))

tf.keras.models.save_model(
    model,
    export_path,
    overwrite=True,
    include_optimizer=True,
    save_format=None,
    signatures=None,
    options=None
)

print('\nSaved model:')


os.environ["MODEL_DIR"] = MODEL_DIR
print(os.environ["MODEL_DIR"])

import json

p="FreeMsg Why haven't you replied to my text? I'm Randy, sexy, female and live local. Luv to hear from u. Netcollex Ltd 08700621170150p per msg reply Stop to enda"
testing_context= remove_stopwords(p)
txts=tok.texts_to_sequences([testing_context])
data = json.dumps({"signature_name": "serving_default", "instances": txts})
print('data :', data)


p="U still going to the mall?"
testing_context= remove_stopwords(p)
txts=tok.texts_to_sequences([testing_context])
data = json.dumps({"signature_name": "serving_default", "instances": txts})
print('data :', data)

import os
os.system("fuser -k 8505/tcp")
os.system('nohup tensorflow_model_server \
  --rest_api_port=8505 \
  --model_name=model \
  --model_base_path="${MODEL_DIR}" >server.log 2>&1')



""" import requests
headers = {"content-type": "application/json"}
data = json.dumps({"signature_name": "serving_default", "instances":txts})
json_response = requests.post('http://localhost:8506/v1/models/model:predict', data=data, headers=headers)
predictions = json.loads(json_response.text)
print(predictions)   """

