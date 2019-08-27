from config import db, ma

class Position(db.Model):
    __tablename__ = 'position'
    id = db.Column(db.Integer, primary_key=True)
    icao24 = db.Column(db.String(10))
    callsign = db.Column(db.String(8), index=True)
    origin_country = db.Column(db.String(50))
    time_position = db.Column(db.Integer, index=True)
    last_contact = db.Column(db.Integer)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    baro_altitude = db.Column(db.Float)
    on_ground = db.Column(db.Boolean)
    velocity = db.Column(db.Float)
    true_track = db.Column(db.Float)
    vertical_rate = db.Column(db.Float)
    sensors = db.Column(db.String(50))
    geo_altitude = db.Column(db.Float)
    squawk = db.Column(db.String(4))
    spi = db.Column(db.Boolean)
    position_source = db.Column(db.Integer)

class PositionSchema(ma.ModelSchema):
    class Meta:
        model = Position
        sqla_session = db.session