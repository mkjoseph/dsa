    def currency_converter(amount, exchange_rate):
        converted_amount = amount * exchange_rate
        six_months_forecast = converted_amount * 1.10  # Assuming a 10% increase in value over six months
        return converted_amount, six_months_forecast