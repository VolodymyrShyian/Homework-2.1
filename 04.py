regular_price = float(input('Enter the regular price: '))
discount = float(input('Enter the discount: '))
percentage_calculation = (regular_price * discount) / 100
discounted_price = regular_price - percentage_calculation
print('discounted price: ', discounted_price)