# linked_list.py


class Node:
    """Node class for a singly linked list/Клас вузла однозв'язного списку"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list/Однозв'язний список"""

    def __init__(self):
        self.head = None

    def append(self, data):
        """Append a new node with the given data to the end of the list/Додає новий вузол з даними в кінець списку"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        """Print all nodes in the list/Виводить усі вузли списку"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def sort(self):
        """Sort the linked list using insertion sort/Сортує список методом вставки"""
        if not self.head or not self.head.next:
            return

        sorted_head = None
        current = self.head
        while current:
            next_node = current.next
            sorted_head = self._sorted_insert(sorted_head, current)
            current = next_node

        self.head = sorted_head

    def _sorted_insert(self, head, node):
        """Insert a node into the sorted part of the list/Вставляє вузол у відсортовану частину списку"""
        if not head or node.data < head.data:
            node.next = head
            return node
        current = head
        while current.next and current.next.data < node.data:
            current = current.next
        node.next = current.next
        current.next = node
        return head


# ==== Testing/Тестування====

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(5)
    ll.append(2)
    ll.append(8)
    ll.append(1)

    print("Original list:")
    ll.print_list()

    ll.sort()
    print("Sorted list:")
    ll.print_list()

# python task1_linked_list/linked_list.py
