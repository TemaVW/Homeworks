# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е.запрашивать все данные у пользователя.
tovaru=[]
nomer=1
zavershenie=''
while zavershenie!='hvatit':
    n=input('vvedite nazvanie')
    c=input('vvedite cenu')
    k=input('vvedite kolichestvo')
    sht=input('vvedite edinitsu izmereniya')
    tovaru.append((nomer,{'nazvanie':n,'cena':c,'kolichestvo':k,"ed":sht}))
    nomer+=1
    zavershenie=input('dlya zaversheniya napishi"hvatit"')
result={}
for number, produts in tovaru:
    for key, value in produts.items():
        if not result.get(key):
            result[key]=[value]
        else:
            result[key].append(value)
for key, value in result.items():
    result[key]=list(set(value))
print(result)