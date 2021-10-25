dannie={'One':'Один',
        'Two':'Два',
        'Three':'Три',
        'Four':'Четыри',
        }

with open("T4_file") as T4:
    with open('new_T4_file.txt','w') as new_file:
        file_lines=T4.readlines()
        for line in file_lines:
            raz=line.split()
            rus_dannie=dannie.get(raz[0])
            new_file.write(f'{line.replace(raz[0],rus_dannie)}')
        #
