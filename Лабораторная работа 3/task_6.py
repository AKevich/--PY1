list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_number = 0
q = 0
for i in range(len(list_numbers)):
    if max_number < list_numbers[i]:
        max_number = list_numbers[i]
        q = i
w = list_numbers[:q] + [list_numbers[-1]] + list_numbers[q+1:len(list_numbers)-1] + [max_number]


print(w)
