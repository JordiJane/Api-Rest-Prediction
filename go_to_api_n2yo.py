from urllib.request import urlopen
import requests
from satelite import Satelite
from typing import List
from positions import Positions
APIKEY = "E8SWFK-FDRUMV-SV6LN2-500F"

def go_to_url():
    r = urlopen("https://api.n2yo.com/rest/v1/satellite/&apiKey=E8SWFK-FDRUMV-SV6LN2-500F")

    print(r.read())
    r.close()

def get_tle():
    response = requests.get("https://api.n2yo.com/rest/v1/satellite/tle/25544&apiKey=E8SWFK-FDRUMV-SV6LN2-500F")
    response.raise_for_status()

    satelite_dict: dict = response.json()

    info = satelite_dict.get("info")
    sat_id = info.get("satid")
    sat_name = info.get("satname")
    transactions_count = info.get("transactionscount")

    satelite : Satelite = Satelite(sat_id, sat_name, transactions_count)

    return satelite

def get_satelit_position():
    response = requests.get("https://api.n2yo.com/rest/v1/satellite/positions/25544/41.702/-76.014/0/2/&apiKey=E8SWFK-FDRUMV-SV6LN2-500F")
    response.raise_for_status()

    satelite_dict: dict = response.json()

    info = satelite_dict.get("info")
    sat_id = info.get("satid")
    sat_name = info.get("satname")
    transactions_count = info.get("transactionscount")

    positions = satelite_dict.get("positions")
    positions_dict = positions[0]
    satlatitude = positions_dict.get("satlatitude")
    satlongitude = positions_dict.get("satlongitude")
    sataltitude = positions_dict.get("sataltitude")
    azimuth = positions_dict.get("azimuth")
    elevation = positions_dict.get("elevation")
    ra = positions_dict.get("ra")
    dec = positions_dict.get("dec")
    timestamp = positions_dict.get("timestamp")
    eclipsed = positions_dict.get("eclipsed")

    satelite: Satelite = Satelite(sat_id, sat_name, transactions_count)

    positions: Positions = Positions(satlatitude, satlongitude, sataltitude, azimuth, elevation, ra, dec, timestamp, eclipsed)

    return satelite, positions