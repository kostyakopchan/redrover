products = {
"apple": {"quantity": 10, "price": 100},
"banana": {"quantity": 20, "price": 50},
"orange": {"quantity": 15, "price": 80},
"grape": {"quantity": 8, "price": 120},
"milk":{"quantity": 12, "price": 90},
"bread": {"quantity": 30, "price": 40}
}

for key in products:
    products[key]["price"] *= 1.2

del products["milk"]

products["Salt"] = {"quantity": 7, "price": 12}

full_price = 0
for key in products:
    full_price += products[key]["quantity"] * products[key]["price"]
    
print(full_price)

#Solution 2
# products = {
#     "apple": {"quantity": 10, "price": 100},
#     "banana": {"quantity": 20, "price": 50},
#     "orange": {"quantity": 15, "price": 80},
#     "grape": {"quantity": 8, "price": 120},
#     "milk":{"quantity": 12, "price": 90},
#     "bread": {"quantity": 30, "price": 40}
# }

# for data in products.values():
#     data["price"] *= 1.2

# del products["milk"]

# products["salt"] = {"quantity": 7, "price": 12}

# total = 0

# for data in products.values():
#     total += data["quantity"] * data["price"]

# print(total)