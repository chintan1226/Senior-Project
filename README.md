# Tweet Sentiment Analysis Guide

## Setup

The first thing to do is to clone the repository:

```
$ git clone https://github.com/chintan1226/Senior-Project.git
$ cd Senior-Project
```

Create a virtual environment to install dependencies in and activate it:

```
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd TweetStockApp
(env)$ python manage.py runserver
```
And navigate to `http://localhost:8000`.

