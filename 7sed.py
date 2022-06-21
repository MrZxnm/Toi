from math import acos, factorial
class Calc:
        expresion=""
        def __init__(self,e='0'):
            self.expresion=e
        def __del__(self):
            self.fn()
        def fn(self):
            print(eval(self.expresion))
while True:
        x=input("\n[acos(x), factorial(x)] Введите пример: ")
        if x=="":
                break
        Calc(x)
