from typing import List, Union

class Queue():
    def __init__(self, input: str):
        self.array = self._fetch_test_data(input)

    def _fetch_test_data(self, input: str) -> List[List[str]]:
        values = list()
        for arr_len in range(2, len(input), 2):
            values.append(input[arr_len:arr_len+2])
        return values

    def _is_array_empty(self) -> bool:
        if len(self.array) == 0:
            return True
        else:
            return False

    def enqueue(self, value: int):
        return self.array.append(value)

    def dequeue(self) -> Union[None, Union[str, int]]:
        if self._is_array_empty():
            print('array is empty')
            return 
        else:
            value = self.array[0]
            self.array = self.array[1:]
            return value


def main():
    input = '5  100\
             p1 150\
             p2 80\
             p3 200\
             p4 350\
             p5 20'
    arr = input.split()
    qms = arr[1]
    queue = Queue(arr)

    answer = list()
    time = 0
    while True:
        first_element = queue.dequeue()
        if first_element is None:
            break
        else:
            time_sub = int(first_element[1]) - int(qms)
            if  time_sub > 0:
                time += int(qms)
                queue.enqueue([first_element[0], time_sub])
            else:
                time += int(first_element[1])
                answer.append([first_element[0], time])
    return answer

if __name__ == '__main__':
    collect = [['p2', 180], ['p5', 400], ['p1', 450], ['p3', 550], ['p4', 800]]
    submit = main()
    assert submit == collect
    print('ok!!')
