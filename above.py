class Above:
    sat_id: int
    sat_name: str
    int_designator: str
    launch_date: str
    sat_lat: float
    sat_lng: float
    sat_alt: float

    def __init__(
        self, sat_id, sat_name, int_designator, launch_date, sat_lat, sat_lng, sat_alt
    ) -> None:
        self.sat_id = sat_id
        self.sat_name = sat_name
        self.int_designator = int_designator
        self.launch_date = launch_date
        self.sat_lat = sat_lat
        self.sat_lng = sat_lng
        self.sat_alt = sat_alt
