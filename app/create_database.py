import MySQLdb
from contextlib import closing

db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="disrupt")

with closing(db.cursor()) as cursor:
	cursor.execute("CREATE TABLE IF NOT EXISTS user_alerts (\
					id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,\
					country_code VARCHAR(30) NOT NULL,\
					number VARCHAR(30) NOT NULL,\
					service VARCHAR(255) NOT NULL,\
					active INT(1),\
					created TIMESTAMP\
					)")
db.commit()
