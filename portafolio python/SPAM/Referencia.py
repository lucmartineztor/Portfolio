

import tensorflow as tf
import os
from keras.models import Sequential
import pickle
import nltk
import joblib
from keras.models import load_model

from dominio import dominio1

model=load_model(dominio1)


import tempfile
""" MODEL_DIR = '/home/desarrollo/Documentos/python/'.join(dominio1) """
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

import os
os.system("fuser -k 8504/tcp")
os.system('nohup tensorflow_model_server \
  --rest_api_port=8504 \
  --model_name=model \
  --model_base_path="${MODEL_DIR}" >server.log 2>&1')



