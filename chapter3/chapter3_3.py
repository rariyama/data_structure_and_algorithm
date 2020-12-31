

def bubble_sort(arr: list, n: int):
    iter_cnt = n
    swap_cnt = 0
    for i in range(iter_cnt):
        for j in range(len(arr)-1, i, -1):
            if arr[j] <= arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
                swap_cnt += 1
    values = ' '.join(map(str, arr))    
    return [values, swap_cnt]

def main():
    input1 = 5
    input2 = '5 3 2 4 1'
    arr = [int(i) for i in input2.split()]

    res = bubble_sort(arr, input1)
    assert res[0] == '1 2 3 4 5'
    assert res[1] ==  8 
    print('ok!!')

if __name__ == '__main__':
    main()