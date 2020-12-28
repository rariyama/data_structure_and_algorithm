

def solve(i: int, m: int, A: list) -> bool:
    if m == 0:
        return True
    elif i == len(A):
        return False
    res = solve(i + 1, m, A) or solve(i + 1, m - A[i], A) # m - arr[i] equals zero
    return res


def main():
    input1 = 5
    input2 = '1 5 7 10 21'
    input3 = 4
    input4 = '2 4 17 8'

    A = [int(i) for i in list(input2.split())]
    M = [int(i) for i in list(input4.split())]

    ans = list()
    for m in M:
        res = solve(0, m, A)
        ans.append(res)        
    return ans


if __name__ == '__main__':
    res = main()
    assert res[0] == False
    assert res[1] == False
    assert res[2] == True
    assert res[3] == True
    print('ok!!')