with open('T2_file') as T2:
    number=0
    for line in T2:
        print(f'{number+1}){line.strip()}')
        sum_words=len(line.split())
        number+=1
        print(f'Сума слов в строке {number}) = {sum_words}\n')
    kol_stroke=number
    print(f'Количество строк="{kol_stroke}"')
    #
