from flask import Flask
import config

app = Flask(__name__)
app.ACCOUNT_SID = config.ACCOUNT_SID
app.AUTH_TOKEN = config.AUTH_TOKEN
app.MY_NUMBER = config.MY_NUMBER
app.TEST_NUMBER = config.TEST_NUMBER
app.DB_HOST = config.DB_HOST
app.DB_USER = config.DB_USER
app.DB_PASSWD = config.DB_PASSWD
app.DB_NAME = config.DB_NAME

from app import views
