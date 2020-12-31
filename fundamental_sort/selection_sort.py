

def selection_sort(arr: list, n: int):
    iter_cnt = n
    swap_cnt = 0
    minimun_pos = 0
    for i in range(iter_cnt-1): # proceed num to the number of array.
        minimun_pos = i # set default value
        for j in range(i+1, iter_cnt): # i+1 means the range is already checked and sorted.  
            if arr[j] < arr[minimun_pos]: # j is smaller than minimum_pos, j becomes minimum.
                minimun_pos = j
        # swap
        temp = arr[i]
        arr[i] = arr[minimun_pos]
        arr[minimun_pos] = temp
        if i != minimun_pos:
            swap_cnt += 1
    values = ' '.join(map(str, arr))    
    return [values, swap_cnt]

def main():
    input1 = 6
    input2 = '5 6 4 2 1 3'
    arr = [int(i) for i in input2.split()]

    res = selection_sort(arr, input1)
    assert res[0] == '1 2 3 4 5 6'
    assert res[1] ==  4
    print('ok!!')

if __name__ == '__main__':
    main()