a = int(input("Введите число равное стороне квадрата:")) 
x = str(input("Выберите тип окружности(вписанная или описанная):"))
r = int(input("Введите радиуc окружности:")) 
y = str(input("Выберите необходимые данные(площадь или длина):"))
import math
pi = math.pi
if x == "вписанная":
    S1 = ((a * 4)/ 2) * r 
    L1 = 2 * pi * r
    if y == "площадь":
        print("Площадь квадрата, который вписан в окружность, равна: ", S1)
    elif y == "длина":
        print("Длина окружности, вокруг которой описан квадрат, равна: ", L1)
elif x == "описанная":
    S2 = 4 * r ** 2
    L2 = 2 * pi * r
    if y == "площадь":
        print("Площадь квадрата, вокруг которого описана окружность, равна: ", S2)
    elif y == "длина":
        print("Длина окружности, внтури которой описан квадрат, равна: ", L2)
else:
    print("Введите верный тип окружности")
P = a * 4
d = 2 ** 1/2 * a
a = r * 3 ** (0.5)
S = (a ** 2 * 3 ** (0.5))/4
print("Площадь вписанного треугольника равна", S)
print("Периметр квадрата равен", P)
print("Длина диагонали квадрата равна", d)

