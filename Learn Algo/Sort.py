def Sorting(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [13,55,14,26,-1,2,80]
size = len(data)
Sorting(data, size)
print('Sorted Array:')
print(data)