# FastAPI

# Bank Note Authentication Problem:

Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.

https://github.com/krishnaik06/FastAPI

To Understand FastAPI, i have downloaded already built project folder from Krish naik Github
So actual python code is MOdelTraining.ipynb. I have already created classifier.pkl file, app.py , requirement.txt , (templates, static not req)
I did deployment by syncing this in my github

## Source Data
##Dataset Link: https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data

## Approach:

By using Linear RandomForset Regressor , we are predicting the JBank Note Authentication based on user input data as 0 or 1
Here we have 4 input value: variance,skewness,curtosis,entropy output class 0 or 1

> 0 means real note, 1 is fake note

Here we used FastAPI web application Framework and deployed in Heroku(PlatformAs A service-PAAS) using gIThUB.


## Here main files are :
		app.py
		model.pkl
		requirements.txt
		Procfile
		Banknotes.py  (This is user defined file. inside we used library - pydantic base model to build the BankNote CLASS
				 to post column name in web)
