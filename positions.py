from flask import request, make_response
from config import db
from models import Position, PositionSchema


#data to be served
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

# handler for get positions
def read():
    """
    This function responds to a request for /api/positions with list of positions

    :return: list of positions
    """
    #create list from table
    position = Position.query.order_by(Position.id.desc()).limit(10).all()

    #Serialise data
    position_schema = PositionSchema(many=True)
    return position_schema.dump(position).data

def create():
    """
    This function handles adding an array on position(s) to the data
    
    :param: positions to be added
    :return: 201 on success and 406 if position already in data
    """
    positions = []
    data = request.json["states"]
    keys = ['icao24', 'callsign', 'origin_country', 'time_position',
            'last_contact', 'longitude', 'latitude', 'baro_altitude',
            'on_ground', 'velocity', 'true_track', 'vertical_rate',
            'sensors', 'geo_altitude', 'squawk', 'spi', 'position_source']
    #if statement regarding adding positions that aren't already there
    for d in data:
        positions.append(dict(zip(keys, d)))

    db.session.bulk_insert_mappings(Position, positions)
    db.session.commit()

    return make_response(
        str(len(data)) + " positions added", 201
    )