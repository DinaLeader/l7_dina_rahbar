inventory = {'apple': 20,
             'banana': 5,
             'orange': 0,
             'milk': 12,
             'bread': 0}

def available_and_unavailable_products(inventory: dict):
    available = []
    unavailable = []

    for product, quantity in inventory.items():
        if quantity > 0:
            available.append(product)
        elif quantity == 0:
            unavailable.append(product)
    return available, unavailable

print(available_and_unavailable_products(inventory)) #(['apple', 'banana', 'milk'], ['orange', 'bread'])


