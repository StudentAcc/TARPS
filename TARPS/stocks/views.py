# import  modules
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TickerForm
from .util import stockChecker, cacheTimeLengthCalculator
from .stockModel import stockModel
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from .recommender import update

# home page view
@login_required
def home(request):

    formNotificationExist = False
    if request.method == 'POST':
        form = TickerForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            timeLength = request.POST['timeLength']
            return HttpResponseRedirect(ticker + '/' + timeLength)
    
    else:
        form = TickerForm()

    context = {'form': form, 'formNotification' : "", 'formNotificationExist' : formNotificationExist}
    
    return render(request, 'stocks/home.html', context)

# stock prediction page view
@login_required
def ticker(request, tickerID, timeLength):
    # render(request, 'stocks/base.html')
    stockPredictionValid, formNotification = stockChecker(tickerID, timeLength)
    formNotificationExist = False
    if (len(formNotification ) > 0):
        formNotificationExist = True
    print(formNotificationExist)
    context = {'form': TickerForm(), 'formNotification' : formNotification, 'formNotificationExist' : formNotificationExist}
    if (not stockPredictionValid):

        return render(request, 'stocks/home.html', context)      # redirect to home page  

    context = {}
    cacheKey = ''
    cacheKey = str(tickerID) + "/" + str(timeLength)
    if(cache.get(cacheKey) == None):
        context['ticker'] = tickerID
        context['timeLength'] = timeLength
        model = stockModel(tickerID, timeLength)
        context['name'] = model.getStockName()
        context['timeLengthSeconds'] = model.timeLengthSeconds
        context['timeLengthName'] = model.timeLengthName
        context['cacheTimeLength'] = context['timeLengthSeconds']
        context['score'], context['risk'] = model.trainModel()
        if (context['score'][0] != "error"):
            if (context['score'][0] != 'issue'):
                context['score'][0] = context['score'][0]
            context['prediction'] = model.predict()
        else:
            context['prediction'] = context['score'][1]
        
        if (not(context['cacheTimeLength'] < 0) and (context['score'][0] != "error") and (context['score'][0] != 'issue')):
            cache.set(cacheKey, context, context['cacheTimeLength'])
            ####### do something for else
            print(context['score'][0])
            print("not cached - now cached")
            print(context['cacheTimeLength'])
    else:
        print("cached - loaded from cache")
        context = cache.get(cacheKey)
        context['cacheTimeLength'] = cacheTimeLengthCalculator(context['timeLengthSeconds'])

    print(cache.get(cacheKey))
    return render(request, 'stocks/ticker.html', context)

# stock recommendation prediction page view
@login_required
def recommendations(request):
    context = {}
    recommendedStocks = []
    if(cache.get('recommendations') != None):
        recommendations = cache.get('recommendations')
        for recommendedStock in recommendations:
            recommendedStocks.append(cache.get(recommendedStock))
        context['stocks'] = recommendedStocks
        context['cacheTimeLength'] = cacheTimeLengthCalculator(recommendedStocks[0]['timeLengthSeconds'])
    # else:
    #     context['stocks'] = False
    # print(context['stocks'][0]['score'])
    return render(request, 'stocks/recommendations.html', context)

# guide page view
@login_required
def guide(request):
    return render(request, 'stocks/guide.html')

