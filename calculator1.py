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

# DRY - Dont repeat Yourself
#dict
options = {1:add,2:sub,3:div,4:mul}
if opr in [1,2,3,4]:
    res = options.get(opr)(x,y)
    print(res)
else:
    print("invalid")