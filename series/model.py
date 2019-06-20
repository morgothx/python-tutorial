from __future__ import absolute_import, division, print_function, unicode_literals
from gensim.corpora import Dictionary
from tensorflow import keras


dictionary = Dictionary.load_from_text('diccionario_gensim.txt')



import spacy
import tensorflow as tf
import keras

import tensorflow as tf
import pandas as pd
import numpy as np
import os

def clean_up(text):
    removal=['ADV','PRON','CCONJ','PUNCT','PART','DET','ADP','SPACE']
    text_out = []
    doc= nlp(text)
    for token in doc:
        if token.is_stop == False and token.is_alpha and len(token)>1 and token.pos_ not in removal:
            lemma = token.lemma_
            text_out.append(lemma)
    return text_out

def procesarString (s, s2):
    text =  [dictionary.doc2idx(clean_up(s)), dictionary.doc2idx(clean_up(s2))]
    train_data = keras.preprocessing.sequence.pad_sequences(text,
                                                        value=0,
                                                        padding='post',
                                                        maxlen=512*2)
    return train_data

nlp = spacy.load("es_core_news_sm")
#x= procesarString(s, s2)
#for y in x:
#    for i in range(1024):
#        if y[i]==-1:
#            y[i]= 2


def create_model( ):
    m = keras.Sequential()
    m.add(keras.layers.Embedding(len (dictionary), 16))
    m.add(keras.layers.GlobalAveragePooling1D())
    m.add(keras.layers.Dense(16, activation=tf.nn.relu))
    m.add(keras.layers.Flatten(input_shape=(1024, )))
    m.add(keras.layers.Dense(25, activation='softmax'))
    m.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['acc'])
    return m

#model2 = create_model()
#import os
#checkpoint_path = "training_1/cp.ckpt"
#checkpoint_dir = os.path.dirname(checkpoint_path)
#model2.load_weights(checkpoint_path)

#tags = ['Kit Cocina', 'Gastos notariales y de documentación', 'Prorroga Alojamiento temporal - Arriendo', 'Kit Dormitorio', 'Gastos de atención en salud', 'Egreso de hotel', 'Visitas para arrendamiento', 'Unidades de redención Alimentación - Aseo', 'Vestuario', 'Servicios funerarios', 'Kit de vivienda saludable ', 'Transporte emergencia', 'Remisión albergue', 'Remision de hotel', 'Orientación oferta distrital', 'Arriendo', 'Prórroga de hotel', 'Alojamiento temporal - Arriendo', 'Remisión Alojamiento temporal - Albergue', 'Prórroga de arriendo', 'Egreso Alojamiento temporal - Albergue', 'Transporte intraUrbano', 'Transporte', 'Kit Vajilla', 'Kit de aseo personal']

#prediction = model2.predict(x[:1])
#for index, num in enumerate ( prediction[0]):
#    print(num, tags[index])


def predict(text):
    clean_up(text)
    procesarString(text, text)
    model2 = create_model()
    checkpoint_path = "training_1/cp.ckpt"
    checkpoint_dir = os.path.dirname(checkpoint_path)
    model2.load_weights(checkpoint_path)
    tags = ['Kit Cocina', 'Gastos notariales y de documentación', 'Prorroga Alojamiento temporal - Arriendo',
            'Kit Dormitorio', 'Gastos de atención en salud', 'Egreso de hotel', 'Visitas para arrendamiento',
            'Unidades de redención Alimentación - Aseo', 'Vestuario', 'Servicios funerarios',
            'Kit de vivienda saludable ', 'Transporte emergencia', 'Remisión albergue', 'Remision de hotel',
            'Orientación oferta distrital', 'Arriendo', 'Prórroga de hotel', 'Alojamiento temporal - Arriendo',
            'Remisión Alojamiento temporal - Albergue', 'Prórroga de arriendo',
            'Egreso Alojamiento temporal - Albergue', 'Transporte intraUrbano', 'Transporte', 'Kit Vajilla',
            'Kit de aseo personal']
    prediction = model2.predict(x[:1])
    ordered =  ( [(prediction[i], tags[i]) for i in range(len(prediction))])
    return ordered.Take(3)
