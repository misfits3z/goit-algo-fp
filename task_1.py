class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    # Реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Зберегти наступний вузол
            current.next = prev  # Змінити посилання на попередній вузол
            prev = current  # Перемістити prev на поточний вузол
            current = next_node  # Перемістити current на наступний вузол
        self.head = prev  # Оновити head на новий перший вузол 

    # Сортування вставками
    def insertion_sort(self):
        sorted_list = None
        cur = self.head

        while cur:
            next_node = cur.next
            sorted_list = self.sorted_insert(sorted_list, cur)
            cur = next_node
        self.head = sorted_list

    def sorted_insert(self, sorted_list, new_node):
        if sorted_list is None or sorted_list.data >= new_node.data:
            new_node.next = sorted_list
            sorted_list = new_node
        else:
            cur = sorted_list
            while cur.next is not None and cur.next.data < new_node.data:
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node
        return sorted_list

    # Об'єднання двох відсортованих списків
    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node()  
        tail = dummy

        while list1 and list2:
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Якщо один із списків закінчився, прикріплюємо залишок іншого списку
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

llist1 = LinkedList()
llist1.insert_at_end(1)
llist1.insert_at_end(3)
llist1.insert_at_end(5)

llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(4)
llist2.insert_at_end(6)

print("Перший відсортований список:")
llist1.print_list()  

print("Другий відсортований список:")
llist2.print_list()  

merged_head = LinkedList.merge_sorted_lists(llist1.head, llist2.head)

merged_list = LinkedList()
merged_list.head = merged_head

print("Об'єднаний відсортований список:")
merged_list.print_list()  


llist3 = LinkedList()
llist3.insert_at_end(3)
llist3.insert_at_end(1)
llist3.insert_at_end(4)
llist3.insert_at_end(2)

print("Невідсортований список:")
llist3.print_list()  

llist3.insertion_sort()
print("Відсортований список:")
llist3.print_list() 


print("Список до реверсування:")
llist3.print_list()  

llist3.reverse()
print("Список після реверсування:")
llist3.print_list()