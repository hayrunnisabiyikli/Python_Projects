class Queue():
    def __init__(self):
        self.size = 0  # Kuyruktaki öğelerin sayısını tutan değişken
        self.list = []  # Kuyruğun kendisini temsil eden liste

    def enqueue(self, data):
        self.list.append(data)  # Öğeyi kuyruğa ekle
        self.size += 1  # Kuyruktaki öğelerin sayısını bir artır

    def dequeue(self):
        try:
            self.size -= 1  # Kuyruktaki öğelerin sayısını bir azalt
            return self.list.pop(0)  # Kuyruğun başındaki öğeyi çıkar ve döndür
        except Exception as error:
            print(f'{error} is not possible')  # Hata durumunda bir hata mesajı yazdır

    def xprint(self, index):
        print(self.list[index])  # Belirtilen indexteki öğeyi ekrana yazdır


def breadth_first(graph, root):
    queue = Queue()  # Queue sınıfından bir kuyruk örneği oluştur
    visited_nodes = list()  # Ziyaret edilen düğümleri tutan liste
    queue.enqueue(root)  # Başlangıç düğümünü kuyruğa ekle
    visited_nodes.append(root)  # Başlangıç düğümünü ziyaret edildi olarak işaretle
    current_node = root  # Şu anki düğüm başlangıç düğümü olarak ayarla

    while queue.size > 0:  # Kuyruk boş olmadığı sürece döngü devam etsin
        current_node = queue.dequeue()  # Kuyruğun başındaki düğümü çıkar ve şu anki düğüm olarak ayarla
        adj_nodes = graph[current_node]  # Şu anki düğümün komşu düğümlerini al
        remaining_elements = sorted(set(adj_nodes) - set(visited_nodes))  # Ziyaret edilmemiş komşu düğümleri belirle

        if len(remaining_elements) > 0:  # Ziyaret edilmemiş düğümler varsa
            for element in remaining_elements:
                visited_nodes.append(element)  # Ziyaret edilen düğümler listesine ekle
                queue.enqueue(element)  # Kuyruğa ekle

    return visited_nodes  # Ziyaret edilen düğümlerin listesini döndür


if __name__ == '__main__':
    graph = dict()

    # Grafın düğümlerini ve bağlantılarını tanımla
    graph['A'] = ['B', 'G', 'D']
    graph['B'] = ['A', 'F', 'E']
    graph['C'] = ['F', 'H']
    graph['D'] = ['F', 'A']
    graph['E'] = ['B', 'G']
    graph['F'] = ['B', 'D', 'C']
    graph['G'] = ['A', 'E']
    graph['H'] = ['C']

    print(breadth_first(graph, 'A'))  # Graf üzerinde genişlik öncelikli arama gerçekleştir
