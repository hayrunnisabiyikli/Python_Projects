def ip_address(address):
    # "ip_address" adında bir işlev tanımlanıyor ve "address" adında bir parametre alıyor.
    new_address = ""
    # "new_address" adında boş bir dize oluşturuluyor.
    split_address = address.split(".")
    # "address" değişkeni noktalara göre bölünerek bir liste haline getiriliyor ve "split_address" adında bir değişkene atanıyor.
    separator = "[.]"
    # "separator" adında bir değişken oluşturuluyor ve değeri "[.]" olarak ayarlanıyor. Bu, noktalar arasına yerleştirilecek bir ayırıcı karakteri temsil ediyor.
    new_address = separator.join(split_address)
    # "split_address" listesindeki elemanlar "separator" karakteriyle birleştirilerek noktalar arasına "[.]" karakteri yerleştiriliyor ve "new_address" değişkenine atanıyor.
    return new_address
    # "new_address" değişkeni işlev tarafından döndürülüyor.

ipaddress = ip_address("1.1.2.3")
# "ip_address" işlevi çağrılıyor ve "1.1.2.3" IP adresi işleniyor. Elde edilen sonuç "ipaddress" adındaki değişkene atanıyor.
print(ipaddress)
# "ipaddress" değişkeninin değeri ekrana yazdırılıyor.
