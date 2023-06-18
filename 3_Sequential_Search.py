def sequential_search(names, target_name):
    found = False
    # Bulunma durumunu tutmak için "found" adında bir mantıksal değişken oluşturuluyor ve başlangıçta "False" olarak ayarlanıyor.
    for name in names:
        # İsimler listesindeki her bir isim için döngüye giriliyor.
        if name == target_name:
            # Eğer isim aranan hedef isme eşitse,
            found = True
            # "found" değişkeni "True" olarak güncelleniyor.
            break
            # Döngüden çıkılıyor, çünkü aranan isim zaten bulunmuştur.
    return found
    # "found" değişkeni işlev tarafından döndürülüyor.

student_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
# Öğrenci isimlerini içeren bir liste oluşturuluyor.
search_name = "Charlie"
# Aranacak olan isim belirleniyor.

result = sequential_search(student_names, search_name)
# "sequential_search" işlevi çağrılıyor ve aranan ismi listede arıyor.
if result:
    print(f"{search_name} is found in the list!")
else:
    print(f"{search_name} is not found in the list.")
# Sonuca göre bir çıktı mesajı ekrana yazdırılıyor.
