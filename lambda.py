#lambda使用例
add_consumption = lambda amount, tax : amount + amount*tax/100
print('Consumption tax : ', add_consumption(100, 8))
