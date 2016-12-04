from contextlib import closing
from app import app
import config
import MySQLdb
import MySQLdb.cursors
from geopy.geocoders import ArcGIS
from geopy.distance import vincenty

def get_user_alerts(service, area):
	db = MySQLdb.connect(host=app.DB_HOST, user=app.DB_USER, passwd=app.DB_PASSWD, db=app.DB_NAME, cursorclass=MySQLdb.cursors.DictCursor)
	with closing(db.cursor()) as cursor:
		cursor.execute("SELECT * FROM user_alerts WHERE service = %s AND area = %s AND active = 1", [service, area])
		data = cursor.fetchall()
	return data

def save_alert(content):
	db = MySQLdb.connect(host=app.DB_HOST, user=app.DB_USER, passwd=app.DB_PASSWD, db=app.DB_NAME, cursorclass=MySQLdb.cursors.DictCursor)
	with closing(db.cursor()) as cursor:
            cursor.execute(
                    "INSERT INTO user_alerts(country_code, phone_number, area, service) VALUES (%s,%s,%s,%s)", 
                    (content['country_code'], content['phone_number'], content['area'], content['service']))
            db.commit()

def save_service(content):
    print content
    address_string = '{address_line_1}, {address_line_2}, {postcode}, {town_city}, {country}'.format(**content)
    geolocator = ArcGIS()
    loc = geolocator.geocode(address_string)
    print loc.raw
    db = MySQLdb.connect(host=app.DB_HOST, user=app.DB_USER, passwd=app.DB_PASSWD, db=app.DB_NAME, cursorclass=MySQLdb.cursors.DictCursor)
    with closing(db.cursor()) as cursor:
        cursor.execute(
                "INSERT INTO services(name, description, email, "
                        "address_line_1, address_line_2, postcode, website, "
                        "area, country, phone_number, town_city, service, "
                        "latitude, longitude) "
                        " VALUES (%s,%s,%s,   %s,%s,%s,%s,'none',%s,%s,%s,%s,%s,%s)", 
                (content['name'], content['description'], content['email'],
                    content['address_line_1'], content['address_line_2'], content['postcode'], content['website'],
                    content['country'], content['phone_number'], content['town_city'], content['service'],
                    loc.latitude, loc.longitude))
        db.commit()

def find_address(coords):
    geolocator = ArcGIS()
    loc = geolocator.reverse(coords)
    return loc.raw['Match_addr']

def search_services(locstring, serv):
    geolocator = ArcGIS()
    loc = geolocator.geocode(locstring)
    p = (loc.longitude, loc.latitude)
    db = MySQLdb.connect(host=app.DB_HOST, user=app.DB_USER, passwd=app.DB_PASSWD, db=app.DB_NAME, cursorclass=MySQLdb.cursors.DictCursor)
    with closing(db.cursor()) as cursor:
        cursor.execute("SELECT * FROM services WHERE service = %s", (serv,))
        data = [ row for row in cursor.fetchall() ]
    for item in data:
        item['distance'] = vincenty(p, (item['longitude'], item['latitude'])).miles
    data.sort(key=lambda x: x['distance'])
    del data[5:]
    return data


