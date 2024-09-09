products = {
"apple": {"quantity": 10, "price": 100},
"banana": {"quantity": 20, "price": 50},
"orange": {"quantity": 15, "price": 80},
"grape": {"quantity": 8, "price": 120},
"milk":{"quantity": 12, "price": 90},
"bread": {"quantity": 30, "price": 40}
}

# Removing milk
del products["milk"]

# Adding Salt
products["Salt"] = {"quantity": 7, "price": 12}

# Adding 20% to price and counting full price
full_price = 0
for key in products:
    products[key]["price"] += products[key]["price"] * 0.2
    full_price += products[key]["quantity"] * products[key]["price"]

print(products)
print(full_price)