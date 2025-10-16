def add(x,y):
    return x+y #return means wapas - >jaha se function call kiya tha waha

def mul(x,y):
    return x*y #return means wapas - >jaha se function call kiya tha waha


def div(x,y):
    return x/y #return means wapas - >jaha se function call kiya tha waha


def sub(x,y):
    return x-y #return means wapas - >jaha se function call kiya tha waha

x = int(input("Enter no1:"))
y = int(input("Enter no2:"))
opr = int(input('''
Press 1 for Addition
Press 2 for Subtraction
Press 3 for Divison
Press 4 for Multiplication : 
                '''))

if opr == 1:
    print(add(x,y))
elif opr == 2:
    print(sub(x,y))
elif opr == 3:
    print(div(x,y))
elif opr == 4:
    print(mul(x,y))
else:
    print("Invalid")