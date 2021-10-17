#Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
chislo=int(input('Vvedite nomer mesyaca:'))
z='zima'
v='vesna'
l='leto'
o='osen'
season_list=[0,z,z,v,v,v,l,l,l,o,o,o,z]
print(season_list[chislo])
season_dict={1:z,2:z,3:v,4:v,5:v,6:l,7:l,8:l,9:o,10:o,11:o,12:z}
print(season_dict[chislo])
