import os
from config import db
from models import Position

#data to initialise db with
positions = [{
                "id": 1,
                "icao24": "ae1fa5",
                "callsign": "72150   ",
                "origin_country": "United States",
                "time_position": 1562968739,
                "last_contact": 1562968739,
                "longitude" : -115.4556,
                "latitude" : 36.3625,
                "baro_altitude" : 1607.82,
                "on_ground" : False,
                "velocity" : 59.57,
                "true_track" : 126.57,
                "vertical_rate" : -3.9,
                "sensors" : 'null',
                "geo_altitude" : 1645.92,
                "squawk" : 'null',
                "spi" : False,
                "position_source" : 0
            },{
                "id": 2,
                "icao24": "ae1fa6",
                "callsign": "72151   ",
                "origin_country": "New Zealand",
                "time_position": 1562968741,
                "last_contact": 1562968741,
                "longitude" : -110.4556,
                "latitude" : 32.3625,
                "baro_altitude" : 1600.00,
                "on_ground" : False,
                "velocity" : 50.57,
                "true_track" : 166.57,
                "vertical_rate" : -2.9,
                "sensors" : 'null',
                "geo_altitude" : 1600.00,
                "squawk" : 'null',
                "spi" : False,
                "position_source" : 0
            },{
                "id": 3,
                "icao24": "ae1fa7",
                "callsign": "72152   ",
                "origin_country": "Australia",
                "time_position": 1562968745,
                "last_contact": 1562968745,
                "longitude" : -100.4556,
                "latitude" : 30.3625,
                "baro_altitude" : 0.00,
                "on_ground" : True,
                "velocity" : 10.00,
                "true_track" : 100.57,
                "vertical_rate" : 0.0,
                "sensors" : 'null',
                "geo_altitude" : 0.00,
                "squawk" : 'null',
                "spi" : False,
                "position_source" : 0
            }]

#delete db if exists
if os.path.exists('position.db'):
    os.remove('position.db')

#create db
db.create_all()

#add initial data
db.session.bulk_insert_mappings(Position, positions)
db.session.commit()
