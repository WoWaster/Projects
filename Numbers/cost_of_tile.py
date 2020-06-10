# Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would
# take to cover a floor plan of width and height, using a cost entered by the user.

print("Программа для подсчета стоимости покрытия пола плитки.")

# Entering all values
price = float(input("Введите цену за плитку:350 "))
tile_width = float(input("Введите ширину плитки:30 "))
tile_height = float(input("Введите длину плитки:50 "))
floor_width = float(input("Введите ширину пола:5 "))
floor_height = float(input("Введите длину пола: 6"))

# Find area of tile and floor
tile_area = tile_height * tile_width
floor_area = floor_height * floor_width

# Make the final calculation
amount = round(floor_area / tile_area)
cost = price * amount

print("Итоговая стоимость покрытия пола:", cost)
