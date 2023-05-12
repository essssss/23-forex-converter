from forex_python.converter import CurrencyRates, CurrencyCodes


def conversion_function(cur_from, cur_to, amt):
    c = CurrencyRates()

    return round(c.convert(cur_from, cur_to, amt), 2)


def validate_cur_code(currency):
    c = CurrencyCodes()
    if c._get_data(currency):
        return True
    return False


def append_symbol(cur_code, amount):
    c = CurrencyCodes()
    symbol = c.get_symbol(cur_code)
    if symbol in ["$", "\u00a3", "\u00a5", "\u20ac"]:
        return str(symbol) + str(amount)
    return str(amount) + str(symbol)
