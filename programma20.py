r = int(input("Введите радиус конуса:")) 
h = int(input("Введите высоту конуса:")) 
l = int(input("Введите длину окружности конуса:")) 
import math
pi = math.pi
V = 1/3 * pi * r ** (2) * h
S = 1/3 * pi * r * l
print("Объем конуса равен", V)
print("Площадь боковой поверхности конуса равна", S)
