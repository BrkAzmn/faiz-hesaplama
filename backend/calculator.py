def calculate_compound_interest(principal, rate, years, compound_frequency=1):
    """
    Bileşik faiz hesaplama formülü:
    A = P * (1 + r/n)^(n*t)
    """
    amount = principal * (1 + rate / (100 * compound_frequency))**(compound_frequency * years)
    return round(amount, 2)
