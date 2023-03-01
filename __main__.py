from go_to_api_n2yo import go_to_url, get_tle, get_satelit_position


def main():
    go_to_url()
    satelite = get_tle()
    print("\n")
    print("Tle")
    print("Satelite ID:", satelite.sat_id)
    print("Satelite Name:", satelite.sat_name)
    print("Satelite Transactions Count:", satelite.transactions_count)
    print("\n")
    satelite2, positions = get_satelit_position()
    print("Satelite info")
    print("Satelite ID:", satelite2.sat_id)
    print("Satelite Name:", satelite2.sat_name)
    print("Satelite Transactions Count:", satelite2.transactions_count)
    print("Satelito Positions")
    print("satlatitude:", positions.satlatitude)
    print("satlongitude:", positions.satlongitude)
    print("sataltitude:", positions.sataltitude)
    print("azimuth:", positions.azimuth)
    print("elevation:", positions.elevation)
    print("ra:", positions.ra)
    print("dec:", positions.dec)
    print("timestamp:", positions.timestamp)
    print("eclipsed", positions.eclipsed)


if __name__ == "__main__":
    # This code won't run if this file is imported.
    main()
