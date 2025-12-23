class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    #  Güncelleme işlemi
    def update(self, old_value, new_value):
        temp = self.head
        updated = False
        while temp:
            if temp.data == old_value:
                temp.data = new_value        # Değeri değiştir
                print(f"{old_value} → {new_value} olarak güncellendi")
                updated = True
            temp = temp.next
        if not updated:
            print(f"{old_value} değeri bulunamadı")

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

dll = DoublyLinkedList()
for v in [10, 20, 30, 40]:
    dll.insert(v)
print("Güncellemeden önce:")
dll.display()

dll.update(20, 25)
dll.display()
dll.update(99, 100)

print("Akademik Yapay Zeka")
