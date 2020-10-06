
# 3. Create a function that takes a list and returns a new list with unique elements of the first list.

def unique_list(list):
    unique =[]
    for i in list:
        if i not in unique:
            unique.append(i)
    print(unique)

list = [1, 2, 3, 4, 6, 7, 3, 4, 6, 2]
unique_list(list)