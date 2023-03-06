class Positions:
    sat_latitude: float
    sat_longitude: float
    sat_altitude: float
    azimuth: float
    elevation: float
    ra: float
    dec: float
    timestamp: int
    eclipsed: bool

    def __init__(
        self,
        sat_latitude,
        sat_longitude,
        sat_altitude,
        azimuth,
        elevation,
        ra,
        dec,
        timestamp,
        eclipsed,
    ) -> None:
        self.sat_latitude = sat_latitude
        self.sat_longitude = sat_longitude
        self.sat_altitude = sat_altitude
        self.azimuth = azimuth
        self.elevation = elevation
        self.ra = ra
        self.dec = dec
        self.timestamp = timestamp
        self.eclipsed = eclipsed
