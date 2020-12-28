from typing import Union

import math


def binary_search(arr: list, key: int) -> Union[int, None]:
    left = 0
    right = len(arr) + 1
    while left < right:
        mid = int((left + right) / 2)
        if arr[mid] == key:
            return 1
        elif key < arr[mid]:
            right = mid
        else:
            left = mid + 1
    print('not found')
    return 



def main():
    input = "5\
             1 2 3 4 5\
             3\
             3 4 1"
    input = input.replace(' ', '')
    list_len_1 = int(input[0])
    contents_1 = [int(i) for i in list(input[1:list_len_1+1])]
    contents_2 = [int(i) for i in list(input[list_len_1+2:])]

    ans = 0
    for content in contents_2:
        res = binary_search(contents_1, content)
        if res is not None:
            ans += int(res)
        else:
            continue
    print(ans)

    return ans


if __name__ == '__main__':
    res = main()
    assert res == 3
    print('ok!!')