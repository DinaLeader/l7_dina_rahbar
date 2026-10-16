products = {
'laptab': 1200,
'phone': 800,
'tablet': 500,
'headphone': 150,
'mouse': 50 }
def find_max_in_dict(products : dict) :
    product_values = list(products.values())
    max_value = max(product_values)
    return max_value


print(find_max_in_dict(products)) #1200




#b
def find_max_product_in_dict(products : dict) :
    max_price = 0
    max_product = ''
    for product, price in products.items():
        if price > max_price :
            max_price = price
            max_product = product
    return max_product


print(find_max_product_in_dict(products)) #laptab




#c
def find_min_in_dict(products : dict) :
    product_values = list(products.values())
    min_value = min(product_values)
    return min_value



print(find_min_in_dict(products)) #50




#d
def find_min_in_product_dict(products : dict) :
    min_price = 1200
    min_product = ''
    for product, price in products.items():
        if price < min_price :
            min_price = price
            min_product = product
    return min_product


print(find_min_in_product_dict(products)) #mouse




#e
def find_sum_in_dict(products : dict) :
        product_values = list(products.values())
        sum_value = sum(product_values)
        return sum_value


print(find_sum_in_dict(products)) #2700





#f
def find_mean_in_dict(products: dict):
    prices = list(products.values())
    return sum(prices) / len(prices)

print(find_mean_in_dict(products)) #540.0


