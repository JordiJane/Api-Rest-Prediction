from go_to_api_n2yo import go_to_url, get_tle
def main():
    go_to_url()
    satelite = get_tle()
    print("Satelite ID:", satelite.sat_id)
    print("Satelite Name:", satelite.sat_name)
    print("Satelite Transactions Count:", satelite.transactions_count)
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()