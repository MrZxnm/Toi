import math
import random
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n
def calc():
    req=input(": ")
    print(eval(req))
while(True):
    o=input('''
Введите номер операций:
"1. +,-,/,*,**,abs"
"2. факториал"
"3. арккосинус"
"4. рандомное число"
: ''')
    if o=="":
        break
    if o=="1":
        calc()
    if o=="2":
        print(fac(int(input(": "))))
    if o=="3":
        try:
            print(math.acos(float(input(": "))))
        except ValueError:
            print("Число должно быть от -1 до 1")
    if o=="4":
        print(random.uniform(-1000, 1000))

