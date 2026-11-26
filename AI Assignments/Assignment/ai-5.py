def calculate_discount(price):
    if price > 1000:
        return price - (price * 10 / 100)
    return price


# Test cases
print(calculate_discount(800))   # 800
print(calculate_discount(1500))  # 1350.0