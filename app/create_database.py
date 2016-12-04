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
	cursor.execute("INSERT INTO user_alerts SET country_code = '+44', phone_number = '7749068166', area = 'shoreditch', service = 'events'")
db.commit()

with closing(db.cursor()) as cursor:
	cursor.execute("CREATE TABLE IF NOT EXISTS services (\
					id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,\
					area VARCHAR(255),\
					service VARCHAR(255),\
					name VARCHAR(255),\
					description VARCHAR(255),\
					email VARCHAR(255),\
					website VARCHAR(255),\
					phone_number VARCHAR(255),\
					address_line_1 VARCHAR(255),\
					address_line_2 VARCHAR(255),\
					town_city VARCHAR(255),\
					country VARCHAR(255),\
					postcode VARCHAR(255),\
					latitude VARCHAR(255),\
					longitude VARCHAR(255),\
					active INT(1) DEFAULT 1,\
					created TIMESTAMP\
					)")
db.commit()

services = [{"area": "west kensington", "service": "dentist", "name": "Family Dentists Ltd", "description": "Family dentists - call to book now", "email": "we_like_teeth@shiny.com", "phone_number": "+448877766655", "website": "www.weloveteeth.com", "address_line_1": "12 Long Road", "address_line_2": "", "town_city": "London", "country": "UK", "postcode": "SE11ES", "latitude": "", "longitude": ""}]
			# {"area": "west kensington", "service": "florists", "name": "Flower Power", "description": "Selling fresh flowers 247", "email": "pink@daisies.com", "phone_number": "+441122233344", "website": "www.flowerpower.com" "address_line_1": "14 Long Road", "address_line_2": "", "town_city": "London", "country": "UK", "postcode": "SE22ES"}]

for service in services:
	with closing(db.cursor()) as cursor:
		cursor.execute("INSERT INTO services SET area = %s, service = %s, name= %s, description = %s, email = %s, website = %s, phone_number = %s", [service['area'], service['service'], service['name'], service['description'], service['email'], service['website'], service['phone_number']])
	db.commit()
