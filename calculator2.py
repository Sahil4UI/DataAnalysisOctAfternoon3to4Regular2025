def calculator(x,opr,y):
    return x+opr+y

x = input("Enter no1:")
y = input("Enter no2:")
opr = input('''
Press + for Addition
Press - for Subtraction
Press / for Divison
Press * for Multiplication : 
                ''')
res = eval(calculator(x,opr,y))
print(res)