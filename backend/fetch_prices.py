import requests

def get_gold_price(year, investment):
    # Örnek API entegrasyonu, API bulunamazsa manuel veri kullanılır
    prices = {2020: (1500, 1900), 2021: (1900, 1800)}  # (Başlangıç, Bitiş)
    price_start, price_end = prices.get(year, (0, 0))

    return round(investment * (price_end / price_start), 2) if price_start else 0

def get_silver_price(year, investment):
    prices = {2020: (18, 25), 2021: (25, 22)}
    price_start, price_end = prices.get(year, (0, 0))

    return round(investment * (price_end / price_start), 2) if price_start else 0
