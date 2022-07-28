# Write a sorting function without using the list.sort function (descending order)

data_list = [24, 55, 78, 64, 25, 12, 22, 11, 1, 2, 44, 3, 122, 23, 25]
new_list = []

while data_list:
    minimum = data_list[0]
    for num in data_list:
        if num > minimum:
            minimum = num
    new_list.append(minimum)
    data_list.remove(minimum)

print(new_list)