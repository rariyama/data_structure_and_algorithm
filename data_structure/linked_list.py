import unittest

# each element of list
class Cell:
    def __init__(self, value):
        '''
        self.value means actural value array has.
        self.next means pointer to the next elements of array
        value|next -> value|next ...
        '''
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Cell(None)

    def insert(self, value):
        front = self.head
        rear = front.next
        while rear and value > rear.value:
            front = rear
            rear = rear.next
        cell = Cell(value)
        cell.next = rear
        front.next = cell

    def delete(self, value):
        front = self.head
        rear = front.next
        while rear:
            if rear.value == value:
                break
            front = rear
            rear = rear.next
        if not rear:
            print("[*] Data not found")
            return 
        front.next = rear.next
        rear = None

    def show(self):
        return_value = list()
        tmp = self.head.next
        while tmp:
            return_value.append(tmp.value)
            tmp = tmp.next
        return return_value


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.test_data = [{'i': 3}, {'i': 5}, {'i': 1}, {'d': 3}]
        self.collect = [1, 5]

    def test_linked_list(self):
        ll = LinkedList()
        for data in self.test_data:
            for kind, value in data.items():
                if kind == 'i':
                    ll.insert(value)
                elif kind == 'd':
                    ll.delete(3)
        self.assertEqual(ll.show(), self.collect)

if __name__ == '__main__':
    unittest.main()