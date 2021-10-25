with open('T3_file') as T3:
    file_lines=T3.readlines()
    sotrudniki={}
    sum_dohod=0
    for line in file_lines:
        dannie=line.split()
        sotrudniki.update({dannie[0]:int(dannie[1])})
        sum_dohod+=int(dannie[1])
sred_dohod=sum_dohod/len(sotrudniki)
print(f'Средний доход = {sred_dohod}')
for s,d in sotrudniki.items():
    if d<20000:
        print(f'{s}-{d}')