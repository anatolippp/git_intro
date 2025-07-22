
def calc():  
    x, y = int(input()), int(input())
    ins = input('Enter "sum" or "min" or "sqrt" or "del"')
    if ins == "sum":
        z = x + y  
        print(f'summa: {z}')
    if ins == "min":
        z = x - y
        print(f'min: {z}')
    if ins == "sqrt":
        z = x*y
        print(f'sqrt: {z}')
    if ins == "del":
        if y != 0:
            z = x/y
            print(f'del: {z}')
        else:
            print('def 0 - bad operation')



calc()
