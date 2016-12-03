import MySQLdb
from contextlib import closing

db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="disrupt")

with closing(db.cursor()) as cursor:
	cursor.execute("CREATE TABLE IF NOT EXISTS user_alerts (\
					id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,\
					country_code VARCHAR(30) NOT NULL,\
					phone_number VARCHAR(30) NOT NULL,\
					area VARCHAR(255),\
					service VARCHAR(255),\
					active INT(1) DEFAULT 1,\
					created TIMESTAMP\
					)")
db.commit()

with closing(db.cursor()) as cursor:
	cursor.execute("INSERT INTO user_alerts SET country_code = '+44', phone_number = '07749068166', area = 'shoreditch', service = 'events'")
db.commit()
