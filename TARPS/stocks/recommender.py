from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from .stockModel import stockModel
from django.core.cache import cache
from .util import cacheTimeLengthCalculator

timeLength = "1d"

# stockSymbols = ["AAPL","TSLA","F","GOOGL"]

# stockSymbols = ['AAPL','TSLA','F',
#                 'GOOGL','AMZN','MSFT',
#                 'FB','TWTR','INTC',
#                 'NIO','NVDA','AMD']

stockSymbols = ['AAPL','TSLA','F',
                'GOOGL','AMZN','MSFT']


def start():
    # update()
    scheduler = BackgroundScheduler()
    scheduler.add_job(update, 'cron', day_of_week='mon-fri', hour=0, minute=0, next_run_time = (datetime.now() + timedelta(seconds = 10)) )
    # scheduler.add_job(test, 'interval', seconds = 10)
    scheduler.start()
    print("-------")

def update():
    models = [[None for x in range(6)] for y in range(len(stockSymbols))] 
    for index in range(len(stockSymbols)):
        cacheKey = str(stockSymbols[index]) + "/" + str(timeLength)
        models[index][0] = stockSymbols[index]
        models[index][1] = stockModel(stockSymbols[index], timeLength)
        models[index][2] = cacheTimeLengthCalculator(models[index][1].timeLengthSeconds)
        if (cache.get(cacheKey) == None):
            models[index][3], models[index][4] = models[index][1].trainModel()
            models[index][5] = models[index][1].predict()
        else:
            models[index][3] = cache.get(cacheKey)['score']
            models[index][4] = cache.get(cacheKey)['risk']
            models[index][5] = cache.get(cacheKey)['prediction']

        cacheKey = models[index][0] + "/" + timeLength
        context = {'ticker': models[index][0], 'timeLength': timeLength, 'timeLengthSeconds': models[index][1].timeLengthSeconds, 'cacheTimeLength' : models[0][2],
                   'prediction': models[index][5], 'name': models[index][1].getStockName(), 'score' : models[index][3], 'risk' : models[index][4], 'timeLengthName': models[index][1].timeLengthName,}
        cache.set(cacheKey, context, models[0][2])
        print(models[index][3], models[index][4])

    if (cache.get('recommendations') == None):

        cacheKeyList = []

        models = sorted(models, key=lambda x: x[3][0])

        for index in range(4):
            # if (models[index][5] == None):
            #     models[index][5] = models[index][1].predict()
            cacheKey = models[index][0] + "/" + timeLength
            cacheKeyList.append(cacheKey)
        
        cache.set('recommendations', cacheKeyList, models[0][2])
    else: 
        return
