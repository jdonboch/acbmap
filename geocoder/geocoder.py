import googlemaps
import random
import string
import json

gmaps = googlemaps.Client(key="<YOUR API KEY>")

with open("acb_country_list.csv", "r") as country_list:
    list_of_addresses = country_list.readlines()

geocode_cache = {}
for address in list_of_addresses:
    try:
        geocode_result = geocode_cache.get(address)
        if not geocode_result:
            print(f"Geocoding {address}...")
            geocode_result = {"geocode": gmaps.geocode(address)[0], "count": 0}
            print(gmaps.geocode(address)[0])
            geocode_cache[address] = geocode_result
        geocode_result["count"] += 1
    except ValueError as e:
        print(e)
        continue


pois = []
country_counts = {}
for address, geocode_result in geocode_cache.items():
    for _ in range(geocode_result["count"]):
        count = geocode_result["count"]
        country_long_name = geocode_result["geocode"]["address_components"][0][
            "long_name"
        ]
        pois.append(
            {
                "label": geocode_result["count"],
                "location": geocode_result["geocode"]["geometry"]["location"],
            }
        )
        if not country_counts.get(country_long_name):
            country_counts[country_long_name] = 0
        country_counts[country_long_name] += 1


with open("pois.json", "w") as pois_file:
    pois_file.write(json.dumps(pois))

with open("geochart_input.json", "w") as geochart_file:
    output = []
    output.append(["Country", "# of Builders"])
    for country, count in country_counts.items():
        output.append([country, count])
    geochart_file.write(json.dumps(output))
