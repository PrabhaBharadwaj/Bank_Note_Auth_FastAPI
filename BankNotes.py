# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float
    
 # Here we are mentioning all web page input col, same way we need to pass in web(Like dictionary value)
""" Ex: 
       {
  "variance": 2,
  "skewness": 3,
  "curtosis": 1,
  "entropy": 4
}"""