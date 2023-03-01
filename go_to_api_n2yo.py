from urllib.request import urlopen
import requests
from satelite import Satelite
from typing import List
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