#Площадь квадрата
import math

def square(side):
    return math.ceil(side * side)

side = int(input("Введите сторону: "))
print(f"Площадь квадрата: {square(side)}")