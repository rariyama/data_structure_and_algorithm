
def merge(left: int, right: int):
    answer = list()
    cnt = 0
    while (len(left) > 0) and (len(right) > 0):
        cnt += 1
        # push value which is smaller than another
        if left[0] < right[0]:
            answer.append(left[0])
            del left[0]
        else:
            answer.append(right[0])
            del right[0]
    if len(left) > 0:
        answer.extend(left)
    else:
        answer.extend(right)
    return answer

def merge_sort(arr: list):
    n = len(arr)
    if  n == 1:
        return arr
    # get the medium position of list
    mid = int(round(n/2))

    left = arr[:mid]
    right = arr[mid:]
    
    # get sub_list
    l = merge_sort(left)
    r = merge_sort(right)
    return merge(l, r)

def main():
    input = '8 5 9 2 6 3 7 1 10 4'
    arr = [int(i) for i in input.split(' ')]
    res = merge_sort(arr)
    return ' '.join(map(str, res))


if __name__ == '__main__':
    res = main()
    print(res)
    assert res == '1 2 3 4 5 6 7 8 9 10'
    print('ok!!')