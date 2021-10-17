# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(a,b,c):
    sum_max=a+b+c-min((a,b,c))
    return sum_max
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=my_func(a,b,c)
print(d)
