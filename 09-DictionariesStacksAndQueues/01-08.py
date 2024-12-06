total_before_discount = 0
total_after_discount = 0
price_list = {
    "T-shirt": 19.99,
    "Jeans": 49.99,
    "Jacket": 89.99,
    "Sneakers": 59.99,
    "Hat": 15.99,
}
for key, value in price_list.items():
    print(f"{key}:{value}")
for key, value in price_list.items():
    total_before_discount += value
print(f"Total before discount: {total_before_discount}")
for key, value in price_list.items():
    price_list[key] = value * 0.9
for key, value in price_list.items():
    print(f"{key}:{value}")
for key, value in price_list.items():
    total_after_discount += value
print(f"Total after discount: {total_after_discount}")
