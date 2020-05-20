def outerFun(a ,b):
    def innerFun(x,y):
        return x+y
    return (innerFun(a,b)+5)
q= int(input("Enter first Number"))
w= int(input("Enter second number"))
print(outerFun(q,w))
