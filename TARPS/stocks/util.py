import yfinance as yf
from time import time
from time import sleep
import numpy as np

# Checks if the stock is in the database and whether it is currently tradeable.
def stockChecker(tickerID, timeLength):
    """
    Checks if the stock is in the database and whether it is currently tradeable.
    """
    stock = yf.Ticker(tickerID)
    data = stock.history(period="1d", interval = "1m")
    return True, ""
    if(len(data) > 0):
        latency = 5
        currentTime = time()
        timeOfLastData = data.index[-1].timestamp()
        timeDifference = time() - data.index[-1].timestamp()
        if (timeLength[-1] == 'm'):
            if (timeDifference > (60 + latency)):
                # return True, ""
                print(currentTime, timeOfLastData, timeDifference)
                return False, "The stock exchange is either closed for this stock or the data is delayed.\nAs a result, intraday predictions for this stock are paused for now. Please try again later."
            # elif(timeDifference > 30):
            #     sleep((60 + latency) - timeDifference)
            #     return stockChecker(tickerID, timeLength)
        
        return True, ""

    else:
        return False, "Stock could not be found."

# Calculates the amount of time to cache the stock / the amount time left until the cache expires.
def cacheTimeLengthCalculator(timeInterval):
    """
    Calculates the amount of time to cache the stock.
    """
    # print(time())
    roundTime = int(np.ceil(time()/timeInterval)) * timeInterval
    return (int(roundTime - time()))
