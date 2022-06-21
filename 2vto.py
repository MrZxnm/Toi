a=input("Введите строку: ")
for b in a:
    print(b)
print(a[:2]+a[3:])
if "с" in a:
    print('В строке есть символ "с"[ru]')
if "c" in a:
    print('В строке есть символ "c"[en]')
print("Длинна строки: "+str(len(a)))
print(a[:len(a)-1])
input()
