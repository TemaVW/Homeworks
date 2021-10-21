from functools import reduce
#my_list=list(range(100,1002,2))
my_list2=[i for i in range(100,1002,2)]
#print(my_list)
print(my_list2)
test_list=[a for a in range(2,12,2)] #2*4*6*8*10=3840
#print(test_list)
def my_func(prev_el,el):
    return prev_el*el
print(f'Тестовий список:{test_list}={reduce(my_func,test_list)}')
def my_func2(pel,elem):
    return pel*elem
print(reduce(my_func2,my_list2))
##
