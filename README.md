# Tweet Sentiment Analysis Guide

Web application that collects Twitter data on specific CEO’s and performs sentiment analysis. In addition, the application display’s the stock value of their company. 


## Setup

The first thing to do is to clone the repository:

```
$ git clone https://github.com/chintan1226/Senior-Project.git
$ cd Senior-Project
```

Create a virtual environment to install dependencies in and activate it:

```
$ virtualenv --no-site-packages env
$ source env/bin/activate
```
Souce: https://docs.python.org/3/library/venv.html

Then install the dependencies:

```
(env)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```
(env)$ cd TweetStockApp
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
And navigate to `http://localhost:8000`.

