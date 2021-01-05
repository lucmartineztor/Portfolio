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
from keras.models import load_model
import tempfile

MODEL_DIR = "/home/desarrollo/Documentos/python/mi.com.co"



text= ""
status= ""
""" texto= "sedjfhifd jhsdfiu hiusyfidhgfik"
Status = "spam" """
def sending_data(texto,Status):
    global text,status
    text=texto
    status=Status
    print("antes",text)
""" function(texto,Status) """
nltk.download('stopwords')
print(text)


stop=stopwords.words ("english")+stopwords.words ("spanish")

def remove_stopwords(EmailText):
	EmailText=[word.lower() for word in EmailText.split() if word.lower() not in stop]
	return " ".join(EmailText)




"""     self.text= pickle.load(open("text","rb")) """
"""     self.status= pickle.load(open("status","rb")) """

spam_value=pickle.load(open("spam_value","rb"))
ham_value=pickle.load(open("ham_value","rb"))
status=pickle.load(open("status","rb"))

max_words=pickle.load(open("max_words","rb"))
model=load_model('network1.h5')
x_train_dictionary=pickle.load(open("x_train","rb"))

# num_classes = max(y_train) + 1
# print(': {}'.format(num_classes))

#max_words = 3800

testing_context= remove_stopwords(text)
max_len=30

print(len(x_train_dictionary))

print(x_train_dictionary[-1],type(x_train_dictionary))

if testing_context not in x_train_dictionary:
    x_train_dictionary=np.append(x_train_dictionary,testing_context)
    pickle.dump(x_train_dictionary,open("x_train","wb"))
    print("ya")

print(len(x_train_dictionary))
tok=Tokenizer(num_words=13000, filters='¡¿!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True)
tok.fit_on_texts(x_train_dictionary)
sequences=tok.texts_to_sequences(x_train_dictionary)
sequences_matrix=sequence.pad_sequences(sequences,maxlen=max_len)



txts=tok.texts_to_sequences([testing_context])
texts=sequence.pad_sequences(txts,maxlen=max_len)


preds=model.predict(texts)
print(preds)


print(texts)

if status=="spam":
    model.train_on_batch(texts, spam_value)
if status=="ham":
    model.train_on_batch(texts, ham_value)

preds=model.predict(texts)
print(preds)
model.save("network1.h5")



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
import os
os.system("fuser -k 8504/tcp")
os.system('nohup tensorflow_model_server \
  --rest_api_port=8504 \
  --model_name=model \
  --model_base_path="${MODEL_DIR}" >server.log 2>&1')
