#Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list=list(input('vvedite znacheniya'))
print(my_list)
kol_elemen=len(my_list)
i=0
if kol_elemen>0:
    while i<kol_elemen-1:
        my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
        i=i+2
print(my_list)
#

