import json


def data():
    with open("currency/currency_codes.json") as f:
        currency_code = json.load(f)

        data = []
        for code, currency in currency_code.items():
            data.append(code.casefold())
            data.append(currency.casefold())

        return data


currency_codes = data()
