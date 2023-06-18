class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# Örnek kullanım
my_queue = Queue()  # Queue oluşturma

my_queue.enqueue("apple")  # "apple" değerini eklemek
my_queue.enqueue("banana")  # "banana" değerini eklemek
my_queue.enqueue("orange")  # "orange" değerini eklemek

print(my_queue.size())  # Kuyruğun boyutunu yazdırmak
print(my_queue.dequeue())  # Kuyruğun başındaki öğeyi çıkarmak ve yazdırmak
print(my_queue.is_empty())  # Kuyruğun boş olup olmadığını kontrol etmek

"""
'is_empty' yöntemi, kuyruğun boş olup olmadığını kontrol eder.
'enqueue' yöntemi, yeni bir öğeyi kuyruğun başına ekler. 
'dequeue' yöntemi, kuyruğun başındaki öğeyi çıkarır ve döndürür. 
'size' yöntemi, kuyruğun boyutunu döndürür.
"""