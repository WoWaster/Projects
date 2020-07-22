# Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would
# take to cover a floor plan of width and height, using a cost entered by the user.

print("Программа для подсчета стоимости покрытия пола плитки.")

# Entering all values
price: float = float(input("Введите цену за плитку: "))
tile_width: float = float(input("Введите ширину плитки: "))
tile_height: float = float(input("Введите длину плитки: "))
floor_width: float = float(input("Введите ширину пола: "))
floor_height: float = float(input("Введите длину пола: "))

# Find area of tile and floor
tile_area: float = tile_height * tile_width
floor_area: float = floor_height * floor_width

# Make the final calculation
amount: float = round(floor_area / tile_area)
cost: float = price * amount

print("Итоговая стоимость покрытия пола:", cost)
