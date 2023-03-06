class Passes:
    start_az: float
    start_az_compass: float
    start_el: float
    start_UTC: int
    max_az: float
    max_az_compass: str
    max_el: float
    max_UTC: int
    end_az: float
    end_az_compass: str
    end_el: int
    end_UTC: int
    mag: float
    duration: int
    start_visibility: int

    def __init__(
        self,
        start_az,
        start_az_compass,
        start_el,
        start_UTC,
        max_az,
        max_az_compass,
        max_el,
        max_UTC,
        end_az,
        end_az_compass,
        end_el,
        end_UTC,
        mag,
        duration,
        start_visibility,
    ) -> None:
        self.start_az = start_az
        self.start_az_compass = start_az_compass
        self.start_el = start_el
        self.start_UTC = start_UTC
        self.max_az = max_az
        self.max_az_compass = max_az_compass
        self.max_el = max_el
        self.max_UTC = max_UTC
        self.end_az = end_az
        self.end_az_compass = end_az_compass
        self.end_el = end_el
        self.end_UTC = end_UTC
        self.mag = mag
        self.duration = duration
        self.start_visibility = start_visibility
