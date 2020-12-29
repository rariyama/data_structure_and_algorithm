

class Sort():
    def _swap(self, arr: list, a: int, b: int):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp


    def partition(self, arr: list, first_pos: int, last_pos: int):
        '''
        compare value with x from left hand side of list.
        if value of list is smaller than x, add current_pos to 1 and swap values.
        if value is equal or bigger than x, swap values and x.
        finally return the position of x.
        ''' 
        x = arr[last_pos]
        current_pos = first_pos - 1
        for p in range(first_pos, last_pos):
            if arr[p] <= x:
                current_pos += 1
                self._swap(arr, current_pos, p)
        self._swap(arr, current_pos+1, last_pos)
        return current_pos + 1

    def quick_sort(self, arr: list, first: int, last: int):
        if first < last:
            # make list into two lists devided by the last value of list
            threshold_pos = self.partition(arr, first, last) 
            # order value of left side of list by using partition functions.
            self.quick_sort(arr, first, threshold_pos - 1)
            # order value of right side of list by using partition functions.
            self.quick_sort(arr, threshold_pos, last)


def main():
    input1 = 12
    input2 = '13 19 9 5 12 8 7 4 21 2 6 11'
    arr = [int(i) for i in input2.split(' ')]
    Sort().quick_sort(arr, 0, len(arr)-1)
    return arr

if __name__ == '__main__':
    res = main()
    assert res == [2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 19, 21]
    print('ok!!')