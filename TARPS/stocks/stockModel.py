# import modules
from tabnanny import verbose
import yfinance as yf
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from django.contrib.staticfiles.storage import staticfiles_storage
import tensorflow as tf
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.utils import shuffle
import math
import os

# stockModel class
class stockModel:
    def __init__(self, ticker, timeLength):
        self.ticker = ticker
        self.name = None
        self.timeLength = timeLength
        self.period, self.timeLengthSeconds, self.timeLengthName = self.timeLengthProcess()
        self.model = None

        self.pricePrediction = True
        self.pastHistory = 5
        self.scaler = None
        self.outputPercentage = False
        self.shuffle = True
    
    # retrieves stock name from yfinance and saves and returns it if need
    def getStockName(self):
        if (self.name is None):
            # self.name = yf.Ticker(self.ticker).info['shortName']  #DOES NOT WORK ANYMORE DUE TO YAHOO FINACNE API CHANGES FAILING TO DECRYPT THE .INFO INFORMATION
            self.name = self.ticker
        return self.name
    
    # loads saved models - USE ONLY FOR TESTING
    def loadModel(self):
        self.model = tf.keras.models.load_model('stocks\static\stocks\saved_model\my_model')
    
    # rounds the time to the nearest time interval specified
    def roundUpTimeToNearest(self, time, timeInterval):
        return int(np.ceil(time/timeInterval)) * timeInterval

    # process the time length
    def timeLengthProcess(self):

        if (self.timeLength == "1m"):
            return '5d', int(self.timeLength[:-1]) * (60), "1 minute"
        elif (self.timeLength == "5m"):
            return '1mo', int(self.timeLength[:-1]) * (60), "5 minutes"
        elif (self.timeLength == "15m"):
            return '1mo', int(self.timeLength[:-1]) * (60), "15 minutes"
        elif (self.timeLength == "30m"):
            return '1mo', int(self.timeLength[:-1]) * (60), "30 minutes"
        elif (self.timeLength == "60m"):
            return '2y', int(self.timeLength[:-1]) * (60), "60 minutes"
        elif (self.timeLength == "1d"):
            return 'max', int(self.timeLength[:-1]) * (60) * 60 * 24, "1 day"
        elif (self.timeLength == "5d"):
            return 'max', int(self.timeLength[:-1]) * (60) * 60 * 24, "5 days"
        elif (self.timeLength == "1mo"):
            return 'max', int(self.timeLength[0]) * (60) * 60 * 24 * 30, "1 month"
    
    # load data from yfinance
    def dataLoad(self):
        stock = yf.Ticker(self.ticker)
        data = stock.history(period= self.period, interval = self.timeLength)
        return data

    # train the model - ORIGINAL IS HIDDEN FOR PRIVACY REASONS
    def trainModel(self):

        print("Contact the developer PRIVATELY for the model training code.")
        return ["error","Contact the developer PRIVATELY for the model training code."], "Contact the developer PRIVATELY for the model training code."

    # Predict the next value of the stock - ORIGINAL IS HIDDEN FOR PRIVACY REASONS
    def predict(self):

        return None