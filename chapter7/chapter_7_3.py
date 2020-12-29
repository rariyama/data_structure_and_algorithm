def partition(arr: list, p:int):
    x = arr[-1]
    i = p - 1
    for p in range(len(arr) - 1):
        if arr[p] <= x:
            i += 1
            temp = arr[i]
            arr[i] = arr[p]
            arr[p] = temp
    temp = arr[i+1]
    arr[i+1] = '[{}]'.format(str(arr[-1]))
    arr[-1] = temp
    return arr


def main():
    input1 = 12
    input2 = '13 19 9 5 12 8 7 4 21 2 6 11'
    arr = [int(i) for i in input2.split(' ')]
    res = partition(arr, 0)
    return res


if __name__ == '__main__':
    res = main()
    ans = ' '.join(map(str, res))
    assert ans == '9 5 8 7 4 2 6 [11] 21 13 19 12'
    print('ok!!')