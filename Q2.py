given = [2, 3, 4, 4, 6, 7, 7]

def dupes(sort_array):
    if not sort_array:
        return []

    L = [sort_array[0]]   #new list L for storing the new singular elements

    for i in range(1, len(sort_array)):
        #this part for checking the dupes
        if sort_array[i] != sort_array[i - 1]:
            L.append(sort_array[i])

    return L

answer = dupes(given)
print(answer)  
