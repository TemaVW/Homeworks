with open('T5_file.txt','w+') as T5:
    T5.write('1 2 3 4 5')
with open('T5_file.txt') as T5:
    dannie=T5.read().split()
    summa=0
    for i in dannie:
        summa += int(i)
print(summa)