# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
name=input('imput name: ')
s_name=input('input second name: ')
year=input('input birthday year: ')
city=input('input city where are you living: ')
email=input('input your email: ')
tel=input('input you number of telephone: ')
def parametru(name,s_name,year,city,email,tel):
    print(f'{name} {s_name} {year} {city} {email} {tel}')
parametru(name=name,s_name=s_name,year=year,city=city,email=email,tel=tel)