import MySQLdb
from contextlib import closing

db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="disrupt")

services = [{"area": "stratford", "service": "dentist", "name": "DentalSpace", "description": "Dental clinic", "email": "dentalspace@gmail.com", "phone_number": "+442085554979", "website": "www.dentalspace.co.uk", "address_line_1": "194 Hugh St", "address_line_2": "Stratford", "town_city": "London", "country": "UK", "postcode": "E15 2NE", "latitude": "51.536000", "longitude": "-0.005081"},
{"area": "stratford", "service": "dentist", "name": "Stratford Village Dental Practice", "description": "Dental clinic", "email": "stratford-dental@gmail.com", "phone_number": "+442085196184", "website": "www.stratford-dental.co.uk", "address_line_1": "42A Romford Rd", "address_line_2": "Stratford", "town_city": "London", "country": "UK", "postcode": "E15 4BZ", "latitude": "51.542086", "longitude": "0.006077"}]
			# {"area": "west kensington", "service": "florists", "name": "Flower Power", "description": "Selling fresh flowers 247", "email": "pink@daisies.com", "phone_number": "+441122233344", "website": "www.flowerpower.com" "address_line_1": "14 Long Road", "address_line_2": "", "town_city": "London", "country": "UK", "postcode": "SE22ES"}]

for service in services:
	with closing(db.cursor()) as cursor:
		cursor.execute("INSERT INTO services SET area = %s, service = %s, name= %s, description = %s, email = %s, website = %s, phone_number = %s, latitude = %s, longitude = %s", [service['area'], service['service'], service['name'], service['description'], service['email'], service['website'], service['phone_number'], service['latitude'], service['longitude']])
	db.commit()
