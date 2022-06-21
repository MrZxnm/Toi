import random
import math
while(True):
    q=input("Введите тип операции(+,-,/,*,^,abs,rand,!,acos): ")
    if q=="":
        break
    if q=="+":
        a=float(input("Введите первое число: "))
        b=float(input("Введите второе число: "))
        print(a+b)
    elif q=="-":
        a=float(input("Введите первое число: "))
        b=float(input("Введите второе число: "))
        print(a-b)
    elif q=="/":
        a=float(input("Введите первое число: "))
        b=float(input("Введите второе число: "))
        print(a/b)
    elif q=="*":
        a=float(input("Введите первое число: "))
        b=float(input("Введите второе число: "))
        print(a*b)
    elif q=="^":
        a=float(input("Введите первое число: "))
        b=float(input("Введите второе число: "))
        print(a**b)
    elif q=="abs":
        a=float(input("Введите число: "))
        print(abs(a))
    elif q=="rand":
        print(random.uniform(-1000, 1000))
    elif q=="!":
        a=int(input("Введите натуральное число: "))
        print(math.factorial(a))
    elif q=="acos":
        a=float(input("Введите число от -1 до 1: "))
        print(math.acos(a))
    else:
        print("Введена неверная операция.")
