#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def del_nums():
    if num2==0:
        return 'na nol delit nelzya'
    else:
        return num1 / num2
num1 = int(input('vvedite pervoe chislo'))
num2 = int(input('vvedite xtoroe chislo'))
print(del_nums())
