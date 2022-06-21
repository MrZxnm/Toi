def sl():
    k=input("Введите список слов: ")
    l=set()
    k=k.split()
    l.update(k)
    return l
a=sl()
print("Кол-во слов: "+str(len(a))+"\nВведите список с таким же кол-вом слов.")
b=sl()
s=dict(zip(a,b))
print(s)
input()
