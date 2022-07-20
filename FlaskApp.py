# -*- coding: utf-8 -*-
"""flask.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IRXpmHgQO1UcYU5rdvs8x3msOf-ZAtD5
"""

import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)
pickle_in = open("regressor.pkl","rb")
regressor=pickle.load(pickle_in)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = regressor.predict(final_features)

    
    return render_template('index.html', prediction_text='The flower belong to species {}'.format(prediction))
    
    


if __name__=='__main__':
    app.run()