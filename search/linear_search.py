

def linear_search(arr: list, key: int):
    i = 0
    arr.append(key)
    n = len(arr) - 1
    while arr[i] != key:
        i += 1
    if i == n:
        return
    return i


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
    for content in contents_1:
        res = linear_search(contents_2, content)
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