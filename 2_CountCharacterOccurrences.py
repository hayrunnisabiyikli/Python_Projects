def count_characters(s):
    # "count_characters" adında bir işlev tanımlanıyor ve "s" adında bir parametre alıyor, bu parametre bir dizedir.
    count = {}
    # "count" adında bir boş sözlük (dictionary) oluşturuluyor.
    for i in s:
        # "s" dizesi üzerindeki her bir karakter için döngüye giriliyor.
        if i in count:
            # Eğer karakter zaten "count" sözlüğünde bulunuyorsa,
            count[i] += 1
            # o karakterin değeri 1 artırılıyor.
        else:
            # Eğer karakter "count" sözlüğünde bulunmuyorsa,
            count[i] = 1
            # o karakter "count" sözlüğüne ekleniyor ve başlangıç değeri 1 olarak atanıyor.
    print(count)
    # "count" sözlüğü ekrana yazdırılıyor.

print(count_characters("It’s so good to see you again"))
# "count_characters" işlevi çağrılıyor ve "It’s so good to see you again" dizesi üzerinde çalıştırılıyor.
