# Реализовать функцию int_func(),
# принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
def int_func(text):
    slovo=text[0].upper+text[1:].lower()
    return slovo
stroka = input('vvedite slova cherez probel')
for slovo in stroka.split(' '):
    print(f'{int_func(slovo)}',end=' ')