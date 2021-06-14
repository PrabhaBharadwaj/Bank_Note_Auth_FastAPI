# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020

@author: win10
"""

# 1. Library imports
import uvicorn  #ASGI
from fastapi import FastAPI
# here BankNotes is BankNotes.py file and import class BankNote inside it to read value from web
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
#@app is fastapi imported object app
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
    #@app is fastapi imported object app
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Prabha''s world': f'{name}'}


# 5. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_banknote(data:BankNote):
    data = data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction="Fake note"
    else:
        prediction="Its a Bank note"
    return {
        'prediction': prediction
    }
    

# 6. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    # Here we use unicorn to run the fastapi object app in local host 127.0.0.1 with port no 8000
    #@app is fastapi imported object app

#Below command used to run this app.py in cmd
    
#uvicorn app:app --reload
    # Here 1st app is filename app.py(If change file name to main, we need to change here also
    # 2nd app is FASTAPI Object name in this file
    #This command we use in cmd to run