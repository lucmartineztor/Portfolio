
from flask import Flask, render_template,request
from flask_restful import Resource, Api
import tensorflow as tf
import os
from keras.models import Sequential
import pickle
import requests
import joblib
from keras.models import load_model
import tempfile
from nltk.corpus import stopwords
from keras.preprocessing.text import Tokenizer
import json

from dominio import dominio1


x_train_dictionary=pickle.load(open("x_train"+dominio1,"rb"))
max_words= pickle.load(open("max_words","rb"))

MODEL_DIR = '/home/desarrollo/Documentos/python/'.join(dominio1) 
""" MODEL_DIR = tempfile.gettempdir()  """
""" version = 1
export_path = os.path.join(MODEL_DIR, str(version))
print('export_path = {}\n'.format(export_path))
 """
tok=Tokenizer(num_words=max_words, filters='¡¿!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True)
tok.fit_on_texts(x_train_dictionary)
sequences=tok.texts_to_sequences(x_train_dictionary)

stop=stopwords.words ("english")+stopwords.words ("spanish")

def remove_stopwords(EmailText):
	EmailText=[word.lower() for word in EmailText.split() if word.lower() not in stop]
	return " ".join(EmailText)



app = Flask (__name__)
@app.route('/')
def index():
    print('llego')
       
    p="Had your mobile 11 months or more? U R entitled to Update to the latest colour mobiles with camera for Free! Call The Mobile Update Co FREE on "
    testing_context= remove_stopwords(p)
    txts=tok.texts_to_sequences([testing_context])
   
    data = json.dumps({"signature_name": "serving_default", "instances":txts})
    print( data)

    json_response = requests.post(url='http://localhost:8504/v1/models/model:predict', data=data)
    """ print(json_response)
    predictions = json.loads(json_response) """ 
    print(json.dumps(json_response.json()))
    return json.dumps(json_response.json())



@app.route('/prediction', methods=['POST'])
def prueba():
    content = request.get_json()
    text = content.get('text')
    print(text)
    
    testing_context= remove_stopwords(text)
    txts=tok.texts_to_sequences([testing_context])
    
    
    data = json.dumps({"instances":txts})
    print( data)

    json_response = requests.post(url='http://localhost:8504/v1/models/model:predict', data=data)
    
    print(json.dumps(json_response.json()))
    return json.dumps(json_response.json())


@app.route('/retraining', methods=['POST'])
def Retraining():
    
    content = request.get_json()
    texto = content.get('text')
    Status = content.get('status') 

    import retraining
    from retraining  import sending_data
    return sending_data(texto,Status)
    
@app.route('/retraintext', methods=['POST'])
def Retraintext():
     
    texto= "Texto de prueba"
    Status= "Texto de prueba"
    import imap
    import retrain_text
    from retrain_text  import sending_data
    return sending_data(texto,Status)
    
@app.route('/retraintextspam', methods=['POST'])
def Retraintextspam():
     
    texto= "Texto de prueba"
    Status= "Texto de prueba"
    import imap_spam
    from imap_spam import sending_data,multiple
    
    """ import retrain_text
    from retrain_text  import sending_data """
    return sending_data(texto,Status)

@app.route('/predtext', methods=['POST'])
def predtext():
    text=pickle.load(open("cleantextSpam"+dominio1,"rb"))
    print(text)
    
    testing_context= remove_stopwords(text)
    txts=tok.texts_to_sequences([testing_context])
    
    
    data = json.dumps({"instances":txts})
    print( data)

    json_response = requests.post(url='http://localhost:8504/v1/models/model:predict', data=data)
    
    print(json.dumps(json_response.json()))
    return json.dumps(json_response.json())

@app.route('/retraintextham', methods=['POST'])
def Retraintextham():
     
    texto= "Texto de prueba"
    Status= "Texto de prueba"
    import imap_ham
    from imap_ham import sending_data,multiple
    """ import retrain_text
    from retrain_text  import sending_data """
    return sending_data(texto,Status)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
