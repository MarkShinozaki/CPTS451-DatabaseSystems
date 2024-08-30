# Mark Shinozaki
# Cpts 451
# This file was used to parse and input data into the milestone1DB 

import json
import psycopg2

def cleanStr4SQL(s):
    return s.replace("'", "''").replace("\n", " ")

def int2BoolStr(value):
    return 'False' if value == 0 else 'True'

def formatArray(arr):
    return "ARRAY[" + ",".join([f"'{cleanStr4SQL(item)}'" for item in arr]) + "]"

def insertData():
    try:
        conn = psycopg2.connect("dbname='milestone1DB' user='postgres' host='localhost' password='jn&!!8tCK6H'")
        cur = conn.cursor()
    except Exception as e:
        print('Unable to connect to the database!', e)
        return

    # Path to your JSON file
    business_file = 'data/yelp_business.JSON'

    # Insert data into business
    with open(business_file, 'r') as f:
        for line in f:
            data = json.loads(line)
            attributes = data.get('attributes', {})
            good_for_meal = attributes.get('GoodForMeal', {})
            ambience = attributes.get('Ambience', {})
            business_parking = attributes.get('BusinessParking', {})

            categories = formatArray(data['categories'])

            sql_str = f"""
            UPDATE business SET
                businessacceptscreditcards = {attributes.get('BusinessAcceptsCreditCards', 'NULL')},
                goodforkids = {attributes.get('GoodForKids', 'NULL')},
                bikeparking = {attributes.get('BikeParking', 'NULL')},
                outdoorseating = {attributes.get('OutdoorSeating', 'NULL')},
                restaurantspricerange2 = {attributes.get('RestaurantsPriceRange2', 'NULL')},
                restaurantsgoodforgroups = {attributes.get('RestaurantsGoodForGroups', 'NULL')},
                hastv = {attributes.get('HasTV', 'NULL')},
                caters = {attributes.get('Caters', 'NULL')},
                wifi = '{cleanStr4SQL(attributes.get('WiFi', 'NULL'))}',
                restaurantsattire = '{cleanStr4SQL(attributes.get('RestaurantsAttire', 'NULL'))}',
                restaurantsreservations = {attributes.get('RestaurantsReservations', 'NULL')},
                restaurantstableservice = {attributes.get('RestaurantsTableService', 'NULL')},
                restaurantstakeout = {attributes.get('RestaurantsTakeOut', 'NULL')},
                restaurantsdelivery = {attributes.get('RestaurantsDelivery', 'NULL')},
                alcohol = '{cleanStr4SQL(attributes.get('Alcohol', 'NULL'))}',
                noiselevel = '{cleanStr4SQL(attributes.get('NoiseLevel', 'NULL'))}',
                goodformeal_breakfast = {good_for_meal.get('breakfast', 'NULL')},
                goodformeal_brunch = {good_for_meal.get('brunch', 'NULL')},
                goodformeal_dessert = {good_for_meal.get('dessert', 'NULL')},
                goodformeal_dinner = {good_for_meal.get('dinner', 'NULL')},
                goodformeal_latenight = {good_for_meal.get('latenight', 'NULL')},
                goodformeal_lunch = {good_for_meal.get('lunch', 'NULL')},
                ambience_romantic = {ambience.get('romantic', 'NULL')},
                ambience_intimate = {ambience.get('intimate', 'NULL')},
                ambience_classy = {ambience.get('classy', 'NULL')},
                ambience_hipster = {ambience.get('hipster', 'NULL')},
                ambience_divey = {ambience.get('divey', 'NULL')},
                ambience_touristy = {ambience.get('touristy', 'NULL')},
                ambience_trendy = {ambience.get('trendy', 'NULL')},
                ambience_upscale = {ambience.get('upscale', 'NULL')},
                ambience_casual = {ambience.get('casual', 'NULL')},
                businessparking_garage = {business_parking.get('garage', 'NULL')},
                businessparking_street = {business_parking.get('street', 'NULL')},
                businessparking_validated = {business_parking.get('validated', 'NULL')},
                businessparking_lot = {business_parking.get('lot', 'NULL')},
                businessparking_valet = {business_parking.get('valet', 'NULL')},
                categories = {categories},
                hours = '{json.dumps(data['hours'])}'
            WHERE business_id = '{cleanStr4SQL(data['business_id'])}';
            """
            try:
                cur.execute(sql_str)
            except Exception as e:
                print("Update to business failed:", e)
            conn.commit()

    cur.close()
    conn.close()

insertData()
