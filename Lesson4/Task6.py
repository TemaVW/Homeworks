from itertools import count as ct
from itertools import cycle
h=(int(input('Введите число от 0 до 9:')))
for el in ct(h):
    if el>10:
        break
    else:
        print(el)
my_list=[1,2,3,4,5]
result=cycle(my_list)
print([next(result) for i in range(20)])

#
