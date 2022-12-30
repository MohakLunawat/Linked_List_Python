class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print('Linked List is empty')
            return
        itr = self.head
        string = ''
        while itr:
            string += str(itr.data) + ' - '
            itr = itr.next
        print(string)
        return

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        return

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
        return

    def insert_at(self, index, data):
        if index == 0:
            self.insert_at_beginning(data)
            return
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index')

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            count += 1
            itr = itr.next

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')
        if index == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data):
        count = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                self.insert_at(count + 1, data)
                return
            count += 1
            itr = itr.next

    def remove_by_value(self, data):
        count = 0
        itr = self.head
        while itr:
            if itr.data == data:
                self.remove_at(count)
                return
            count += 1
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", 5)
    ll.print()
    ll.remove_by_value("orange")
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.print()
    ll.remove_by_value("mango")
    ll.print()
    ll.remove_by_value(5)
    ll.print()
    ll.remove_by_value("grapes")
    ll.print()
