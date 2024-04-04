List_of_number = [-1,15,4,6,2,3,8,10,23,20]

for i in range(len(List_of_number)):
    for j in range(len(List_of_number)):
       if List_of_number[i] < List_of_number[j]:
        temp = List_of_number[i]
        List_of_number[i] = List_of_number[j]
        List_of_number[j] = temp

print(List_of_number)