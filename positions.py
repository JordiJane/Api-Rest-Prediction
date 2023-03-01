class Positions:
    satlatitude: float
    satlongitude: float
    sataltitude: float
    azimuth: float
    elevation: float
    ra: float
    dec: float
    timestamp: int
    eclipsed: bool

    def __init__(self, satlatitude, satlongitude, sataltitude, azimuth, elevation, ra, dec, timestamp, eclipsed) -> None:
        self.satlatitude = satlatitude
        self.satlongitude = satlongitude
        self.sataltitude = sataltitude
        self.azimuth = azimuth
        self.elevation = elevation
        self.ra = ra
        self.dec = dec
        self.timestamp = timestamp
        self.eclipsed = eclipsed