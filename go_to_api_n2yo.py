from urllib.request import urlopen
import requests
from satelite import Satelite
from typing import List
from positions import Positions
from passes import Passes
from above import Above

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

    satelite: Satelite = Satelite(
        sat_id=sat_id, sat_name=sat_name, transactions_count=transactions_count
    )

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

    sat_latitude = positions_dict.get("satlatitude")
    sat_longitude = positions_dict.get("satlongitude")
    sat_altitude = positions_dict.get("sataltitude")
    azimuth = positions_dict.get("azimuth")
    elevation = positions_dict.get("elevation")
    ra = positions_dict.get("ra")
    dec = positions_dict.get("dec")
    timestamp = positions_dict.get("timestamp")
    eclipsed = positions_dict.get("eclipsed")

    satelite: Satelite = Satelite(
        sat_id=sat_id, sat_name=sat_name, transactions_count=transactions_count
    )

    positions: Positions = Positions(
        sat_latitude=sat_latitude,
        sat_longitude=sat_longitude,
        sat_altitude=sat_altitude,
        azimuth=azimuth,
        elevation=elevation,
        ra=ra,
        dec=dec,
        timestamp=timestamp,
        eclipsed=eclipsed,
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

    start_az = passes_dict.get("startAz")
    start_az_compass = passes_dict.get("startAzCompass")
    start_el = passes_dict.get("startEl")
    start_UTC = passes_dict.get("startUTC")
    max_az = passes_dict.get("maxAz")
    max_az_compass = passes_dict.get("maxAzCompass")
    max_el = passes_dict.get("maxEl")
    max_UTC = passes_dict.get("maxUTC")
    end_az = passes_dict.get("endAz")
    end_az_compass = passes_dict.get("endAzCompass")
    end_el = passes_dict.get("endEl")
    end_UTC = passes_dict.get("endUTC")
    mag = passes_dict.get("mag")
    duration = passes_dict.get("duration")
    start_visibility = passes_dict.get("startVisibility")

    satelite: Satelite = Satelite(
        sat_id=sat_id,
        sat_name=sat_name,
        transactions_count=transactions_count,
        passes_count=passes_count,
    )

    passes: Passes = Passes(
        start_az=start_az,
        start_az_compass=start_az_compass,
        start_el=start_el,
        start_UTC=start_UTC,
        max_az=max_az,
        max_az_compass=max_az_compass,
        max_el=max_el,
        max_UTC=max_UTC,
        end_az=end_az,
        end_az_compass=end_az_compass,
        end_el=end_el,
        end_UTC=end_UTC,
        mag=mag,
        duration=duration,
        start_visibility=start_visibility,
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

    start_az = passes_dict.get("startAz")
    start_az_compass = passes_dict.get("startAzCompass")
    start_el = passes_dict.get("startEl")
    start_UTC = passes_dict.get("startUTC")
    max_az = passes_dict.get("maxAz")
    max_az_compass = passes_dict.get("maxAzCompass")
    max_el = passes_dict.get("maxEl")
    max_UTC = passes_dict.get("maxUTC")
    end_az = passes_dict.get("endAz")
    end_az_compass = passes_dict.get("endAzCompass")
    end_el = passes_dict.get("endEl")
    end_UTC = passes_dict.get("endUTC")
    mag = passes_dict.get("mag")
    duration = passes_dict.get("duration")
    start_visibility = passes_dict.get("startVisibility")

    satelite: Satelite = Satelite(
        sat_id=sat_id,
        sat_name=sat_name,
        transactions_count=transactions_count,
        passes_count=passes_count,
    )

    passes: Passes = Passes(
        start_az=start_az,
        start_az_compass=start_az_compass,
        start_el=start_el,
        start_UTC=start_UTC,
        max_az=max_az,
        max_az_compass=max_az_compass,
        max_el=max_el,
        max_UTC=max_UTC,
        end_az=end_az,
        end_az_compass=end_az_compass,
        end_el=end_el,
        end_UTC=end_UTC,
        mag=mag,
        duration=duration,
        start_visibility=start_visibility,
    )

    return satelite, passes


def get_above():
    response = requests.get(
        f"https://api.n2yo.com/rest/v1/satellite/above/41.702/-76.014/0/70/18/&apiKey={APIKEY}"
    )
    response.raise_for_status()

    satelite_dict: dict = response.json()

    info = satelite_dict.get("info")
    sat_id = info.get("satid")
    sat_name = info.get("satname")
    transactions_count = info.get("transactionscount")
    passes_count = info.get("passescount")
    category = info.get("category")
    sat_count = info.get("satcount")

    above = satelite_dict.get("above")
    above_dict = above[0]

    sat_id = above_dict.get("satid")
    sat_name = above_dict.get("satname")
    int_designator = above_dict.get("intDesignator")
    launch_date = above_dict.get("launchDate")
    sat_lat = above_dict.get("satlat")
    sat_lng = above_dict.get("satlng")
    sat_alt = above_dict.get("satalt")

    satelite: Satelite = Satelite(
        sat_id=sat_id,
        sat_name=sat_name,
        transactions_count=transactions_count,
        passes_count=passes_count,
        category=category,
        sat_count=sat_count,
    )

    above: Above = Above(
        sat_id=sat_id,
        sat_name=sat_name,
        int_designator=int_designator,
        launch_date=launch_date,
        sat_lat=sat_lat,
        sat_lng=sat_lng,
        sat_alt=sat_alt,
    )

    return satelite, above
