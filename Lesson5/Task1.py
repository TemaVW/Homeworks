with open('text_file.txt','w') as my_file:
    text=input('\n')
    while text:
        my_file.write(f'{text}\n')
        text = input('\n')