# TARPS - PUBLIC VERSION (STOCK AI MODEL HAS BEEN REDACTED - CONTACT THE REPOSITRY OWNER FOR ACCESS)
TARPS (TARPS - Trend Analysis Recogniser Prediction System) is an AI system which can aid traders to make the most out of historical financial data to be able to predict more accurately the best trades to make. This will try and reduce (not eradicate) the problem of uncertainty which effects traders trading in the stock market.

This will be done via training AI models on existing past financial stock data which will require some pre-processing (which will also be done automatically). These models will then be used to predict the outcomes of future prices of stocks to fair certainty (ideally above 50%) and be able to then recommend what trades are ideal to be made to make the most out of the predictions.

The front-end UI implementation will include a stock ticker and trade duration selector to predict the best trades for your selection and a more general ‘best recommended trades’ screen which advises on the best trades to make currently. 

TARPS will exploit an assumption that there is, at least mostly, a natural order/pattern to how stock prices move.

----

How to run TARPS:

1.	Have python 3.10.4 installed and make it the highest priority in your global environment variables PATH
2.	Open the Supporting documents folder and navigate to the folder TarpsCode
3.	Open a terminal window here
4.	Create a python 3.10.4 virtual environment:
Enter:	py -m venv env
5.	Activate the environemnt:
Enter:	.\env\Scripts\activate
6.	Install dependencies:
Enter:	pip install -r {/path/to/requirements.txt}
7.	Navigate to the Django project:
Enter:	cd TARPS
8.	Start Django local server:
Enter:	python manage.py runserver --noreload  
9.	Navigate to the TARPS web app on your browser:
URL:	http://127.0.0.1:8000/
10.	If a login is required, the credentials are:
Username:	admin
Password:	admin
11.	Enjoy!

-----

Languages:

    • Python (backend)
    • CSS (styling)
    • HTML (frontend)
    • JavaScript (frontend)

Libraries:

    • In-built Python library
    • TensorFlow (incl. Keras)
    • yfinance
    • Numpy
    • Pandas
    • Matplotlib (for testing)
    • Django
    • Scikit-learn
    • Bootstrap (for styling)
