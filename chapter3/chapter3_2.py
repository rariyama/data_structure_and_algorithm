
input = '5 2 4 6 1 3'
arr = [int(i) for i in input.split()]

temp = 0
array_length = len(arr)
for i in range(1, array_length):
    temp = arr[i]
    j  = i - 1
    while j >= 0 and arr[j] > temp:
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = temp



assert arr == [1, 2, 3, 4, 5, 6]
print('ok')