# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
original_list=[300,2,12,44,1,1,4,10,7,1,78,123,55]
result_list=[original_list[i] for i in range(1,len(original_list)) if original_list[i]>original_list[i-1]]
print(result_list)
#
