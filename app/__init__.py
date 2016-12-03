from flask import Flask
from flask_mysqldb import MySQL
import config

app = Flask(__name__)
app.ACCOUNT_SID = config.ACCOUNT_SID
app.AUTH_TOKEN = config.AUTH_TOKEN

mysql = MySQL(app)

from app import views
