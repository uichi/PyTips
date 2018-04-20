#lambda使用例
add_consumption = lambda amount, tax : amount + amount*tax/100
print('Consumption tax : ', add_consumption(100, 8))

num_list = list(range(0,99))
square_list = list(map(lambda x : x**2, num_list))
print(square_list)
