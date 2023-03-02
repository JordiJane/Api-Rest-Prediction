from urllib.request import urlopen
import requests
from satelite import Satelite
from typing import List
from positions import Positions
from passes import Passes

APIKEY = "E8SWFK-FDRUMV-SV6LN2-500F"


def go_to_url():
    r = urlopen(f"https://api.n2yo.com/rest/v1/satellite/&apiKey={APIKEY}")

    print(r.read())
    r.close()


def get_tle():
    response = requests.get(
        f"https://api.n2yo.com/rest/v1/satellite/tle/25544&apiKey={APIKEY}"
    )
    response.raise_for_status()

    satelite_dict: dict = response.json()

    info = satelite_dict.get("info")
    sat_id = info.get("satid")
    sat_name = info.get("satname")
    transactions_count = info.get("transactionscount")

    satelite: Satelite = Satelite(sat_id, sat_name, transactions_count)

    return satelite


def get_satelit_position():
    response = requests.get(
        f"https://api.n2yo.com/rest/v1/satellite/positions/25544/41.702/-76.014/0/2/&apiKey={APIKEY}"
    )
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

    positions: Positions = Positions(
        satlatitude,
        satlongitude,
        sataltitude,
        azimuth,
        elevation,
        ra,
        dec,
        timestamp,
        eclipsed,
    )

    return satelite, positions


def get_visual_passes():
    response = requests.get(
        f"https://api.n2yo.com/rest/v1/satellite/visualpasses/25544/41.702/-76.014/0/2/300/&apiKey={APIKEY}"
    )
    response.raise_for_status()

    satelite_dict: dict = response.json()

    info = satelite_dict.get("info")
    sat_id = info.get("satid")
    sat_name = info.get("satname")
    transactions_count = info.get("transactionscount")
    passes_count = info.get("passescount")

    passes = satelite_dict.get("passes")
    passes_dict = passes[0]

    startAz = passes_dict.get("startAz")
    startAzCompass = passes_dict.get("startAzCompass")
    startEl = passes_dict.get("startEl")
    startUTC = passes_dict.get("startUTC")
    maxAz = passes_dict.get("maxAz")
    maxAzCompass = passes_dict.get("maxAzCompass")
    maxEl = passes_dict.get("maxEl")
    maxUTC = passes_dict.get("maxUTC")
    endAz = passes_dict.get("endAz")
    endAzCompass = passes_dict.get("endAzCompass")
    endEl = passes_dict.get("endEl")
    endUTC = passes_dict.get("endUTC")
    mag = passes_dict.get("mag")
    duration = passes_dict.get("duration")
    startVisibility = passes_dict.get("startVisibility")

    satelite: Satelite = Satelite(sat_id, sat_name, transactions_count, passes_count)

    passes: Passes = Passes(
        startAz,
        startAzCompass,
        startEl,
        startUTC,
        maxAz,
        maxAzCompass,
        maxEl,
        maxUTC,
        endAz,
        endAzCompass,
        endEl,
        endUTC,
        mag,
        duration,
        startVisibility,
    )

    return satelite, passes


def get_radio_passes():
    response = requests.get(
        f"https://api.n2yo.com/rest/v1/satellite/radiopasses/25544/41.702/-76.014/0/2/40/&apiKey={APIKEY}"
    )
    response.raise_for_status()

    satelite_dict: dict = response.json()

    info = satelite_dict.get("info")
    sat_id = info.get("satid")
    sat_name = info.get("satname")
    transactions_count = info.get("transactionscount")
    passes_count = info.get("passescount")

    passes = satelite_dict.get("passes")
    passes_dict = passes[0]

    startAz = passes_dict.get("startAz")
    startAzCompass = passes_dict.get("startAzCompass")
    startEl = passes_dict.get("startEl")
    startUTC = passes_dict.get("startUTC")
    maxAz = passes_dict.get("maxAz")
    maxAzCompass = passes_dict.get("maxAzCompass")
    maxEl = passes_dict.get("maxEl")
    maxUTC = passes_dict.get("maxUTC")
    endAz = passes_dict.get("endAz")
    endAzCompass = passes_dict.get("endAzCompass")
    endEl = passes_dict.get("endEl")
    endUTC = passes_dict.get("endUTC")
    mag = passes_dict.get("mag")
    duration = passes_dict.get("duration")
    startVisibility = passes_dict.get("startVisibility")

    satelite: Satelite = Satelite(sat_id, sat_name, transactions_count, passes_count)

    passes: Passes = Passes(
        startAz,
        startAzCompass,
        startEl,
        startUTC,
        maxAz,
        maxAzCompass,
        maxEl,
        maxUTC,
        endAz,
        endAzCompass,
        endEl,
        endUTC,
        mag,
        duration,
        startVisibility,
    )

    return satelite, passes
