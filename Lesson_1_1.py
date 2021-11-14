
print("Введите число a =")
a = int(input())

print("Введите число b =")
b = int(input())

print("Выберете операцию:")
print("1- сложить a+b")
print("2- вычесть a-b")
print("3- умножить a*b")
print("4- разделить a/b")
d = float(input())

if d==1:
    print("Сумма: a+b =", a+b)

if d==2:
    print("Разность: a-b =", a-b)

if d==3:
    print("Умножение: a*b =", a*b)

if d==4:
    print("Деление: a/b =", a/b)
