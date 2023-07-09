# Stack sınıfının tanımı
class Stack:
    def __init__(self):
        self.items = []  # Boş bir liste oluşturuluyor

    def is_empty(self):
        return self.items == []  # Liste boş mu kontrol ediliyor

    def push(self, item):
        self.items.append(item)  # Öğe listeye ekleniyor

    def pop(self):
        return self.items.pop()  # Listenin sonundan bir öğe çıkarılıp döndürülüyor

    def peek(self):
        l = len(self.items) - 1
        return self.items[l]  # Listenin en üstündeki öğeyi döndürülüyor

    def size(self):
        return len(self.items)  # Listenin boyutu döndürülüyor


# Stack örneğinin oluşturulması
stack = Stack()

# Stack'in boş olup olmadığının kontrolü
print(stack.is_empty())

# 0'dan 9'a kadar olan sayıların Stack'e eklenmesi
for i in range(0, 10):
    stack.push(i)

# Stack'in boyutunun yazdırılması
print(stack.size())

# Stack'in içindeki öğelerin yazdırılması
print(stack.items)
