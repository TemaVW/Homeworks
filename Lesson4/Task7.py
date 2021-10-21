def factorial(n):
    a=1
    for i in range(1, n+1):
        a*=i
        yield a

b=4
for el in factorial(b):
    print(el)
    ##
