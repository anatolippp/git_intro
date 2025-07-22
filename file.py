
def calc():  
    x, y = int(input()), int(input())
    ins = input('Enter "sum" or "min" or "sqrt" or "del"')
    if ins == "sum":
        z = x + y  
        print(f'summa: {z}')
    if ins == "min":
        z = x - y
        print(f'min: {z}')

calc()
