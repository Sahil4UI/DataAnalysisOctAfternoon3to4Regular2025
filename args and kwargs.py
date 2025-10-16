# def f1(x,y=0):
#     print(x,y)
# # y is optional parameter
# f1(1)

# # * argument
# def f2(x,*y):
#     print(x,y)
# # y is optional parameter
# f2(1,2,3,4,45)

#** kwargs - keyworded arguments

def f2(roll,name,**optional):
    print(roll,name,optional)
# y is optional parameter
f2(1,"Ravi",fname="suresh",age="16",contact="9876543210")