'''
Created on Jan 21, 2018

@author: karan
'''
import requests
import pymysql


def find():
# Open database connection
    db = pymysql.connect("localhost","<username>","<password>","<dbname>")

    cursor = db.cursor()

# Create table as per requirement
    sql = ('SELECT * FROM <tablename> where id>1 and id<3')
    cursor.execute(sql)
    data=cursor.fetchall()
    print(data)

# Fetch all the data returned by the database query as a list

    address =data
    api_key = "<API_KEY>"
    api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
    api_response_dict = api_response.json()

    if api_response_dict['status'] == 'OK':
        latitude = api_response_dict['results'][0]['geometry']['location']['lat']
        longitude = api_response_dict['results'][0]['geometry']['location']['lng']
        print('Latitude:', latitude)
        print('Longitude:', longitude)
        return latitude


res= find()           
