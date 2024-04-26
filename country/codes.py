import json


def data():
    with open("country/country_codes.json") as f:
        country_code = json.load(f)

        data = []
        for code, country in country_code.items():
            data.append(code.casefold())
            data.append(country.casefold())

        return data


country_codes = data()
