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
from dominio import dominio1



global text,status

text= "Texto de prueba"
status= "Texto de prueba"

def sending_data(texto,Status):
    
    global text,status
    Status="spam"
    texto=pickle.load(open("cleantextSpam"+dominio1,"rb"))
    text=texto
    status=Status
    print("antes: ",text)
    func(text,status)
    return text,status


def remove_stopwords(EmailText):
    
    stop=stopwords.words ("english")+stopwords.words ("spanish")
    EmailText=[word.lower() for word in EmailText.split() if word.lower() not in stop]
    return " ".join(EmailText)



def func(text,status):
    nltk.download('stopwords')
    print("despues: ",text)

    
    spam_value=pickle.load(open("spam_value","rb"))
    ham_value=pickle.load(open("ham_value","rb"))
    max_words= pickle.load(open("max_words","rb"))
    model=load_model(dominio1)
    x_train_dictionary=pickle.load(open("x_train"+dominio1,"rb"))

    # num_classes = max(y_train) + 1
    # print(': {}'.format(num_classes))

    #max_words = 3800

    testing_context= remove_stopwords(text)
    max_len=30
    print(len(x_train_dictionary))

    """ print(x_train_dictionary[-1],type(x_train_dictionary)) """

    if testing_context not in x_train_dictionary:
        x_train_dictionary=np.append(x_train_dictionary,testing_context)
        pickle.dump(x_train_dictionary,open("x_train"+dominio1,"wb"))
        print("Realizado los cambios al diccionario de frases")

    """ print(x_train_dictionary[-1],type(x_train_dictionary)) """
    print(len(x_train_dictionary))
    tok=Tokenizer(num_words=max_words, filters='¡¿!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True)
    tok.fit_on_texts(x_train_dictionary)
    sequences=tok.texts_to_sequences(x_train_dictionary)
    sequences_matrix=sequence.pad_sequences(sequences,maxlen=max_len) 

    txts=tok.texts_to_sequences([testing_context])
    texts=sequence.pad_sequences(txts,maxlen=max_len)

    preds=model.predict(texts)
    print(preds, status)

    print(texts)

    if status=="spam":
        model.train_on_batch(texts, spam_value)
        
    if status=="ham":
        model.train_on_batch(texts, ham_value)
        
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
    print("prediccion pre-training: ",preds)
    preds=model.predict(texts)
    print("prediccion post-training: ",preds)
    os.environ["MODEL_DIR"] = MODEL_DIR
        
    return text
