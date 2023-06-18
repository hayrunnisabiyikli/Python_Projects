class HashTable:
    def __init__(self, items):
        self.bucket_size = len(items)  # Öğelerin saklanacağı bucket sayısı
        self.buckets = [[] for _ in range(self.bucket_size)]  # Bucket listesi
        self.assign_buckets(items)  # Öğeleri bucket lara atama işlemi

    def assign_buckets(self, items):
        for key, value in items:
            hash_value = hash(key)  # Anahtarın hash değerini hesaplama
            index = hash_value % self.bucket_size  # Hash değeriyle indeks belirleme
            self.buckets[index].append((key, value))  # Öğeyi ilgili bucket a ekleme

    def get_value(self, input_key):
        hash_value = hash(input_key)  # Aranan anahtarın hash değerini hesaplama
        index = hash_value % self.bucket_size  # Hash değeriyle indeks belirleme
        bucket = self.buckets[index]  # İlgili bucket ı alma
        for key, value in bucket:
            if key == input_key:  # Anahtar eşleşmesi kontrolü
                return value  # Eşleşme bulunduğunda değeri döndürme
        return None  # Eşleşme yoksa None döndürme

# Örnek kullanım
items = [("apple", 5), ("banana", 3), ("orange", 7)]  # Anahtar-değer çiftlerini içeren liste

my_table = HashTable(items)  # Hashtable oluşturma

value = my_table.get_value("apple")  # "apple" anahtarına karşılık gelen değeri alma
print(value)  # 5
