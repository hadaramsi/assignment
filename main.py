# Price Check function

def PriceCheck(products, productPrices, productSold, soldPrice):
    incorrectlyPrices = 0
    for i, product in enumerate(productSold):
        if (productPrices[products.index(product)]) != soldPrice[i]:
            incorrectlyPrices += 1
    return incorrectlyPrices


# Example of Function Call
print(PriceCheck(['rice', 'sugar', 'wheat', 'cheese'], [16.89, 56.92, 20.89, 345.99], ['rice', 'cheese'], [18.99, 400.89]))
print(PriceCheck(['rice', 'sugar', 'wheat', 'cheese'], [16.89, 56.92, 20.89, 345.99], ['rice', 'cheese'], [16.89, 400.89]))
print(PriceCheck(['rice', 'sugar', 'wheat', 'cheese'], [16.89, 56.92, 20.89, 345.99], ['rice', 'cheese', 'wheat'], [16.89, 345.99, 20.89]))


# ----------------------------------------------------------------------------------------------------

# summer function

def summer(num):
    if num == 0:
        return 0
    return (num % 10) + summer(int(num/10))


res = summer(2347623)
print(res)
