def anagram(word1, word2):
    # Her iki kelimeyi küçük harflere dönüştürmek için lower() fonksiyonunu kullanıyoruz.
    word1 = word1.lower()
    word2 = word2.lower()

    # Sıralanmış kelimelerin karşılaştırılması ile anagram olup olmadığı kontrol ediliyor.
    return sorted(word1) == sorted(word2)


# Örnek 1: "cinema" ve "iceman" birbirinin anagramıdır.
print(anagram("cinema", "iceman"))  # True

# Örnek 2: "cool" ve "loco" birbirinin anagramıdır.
print(anagram("cool", "loco"))  # True

# Örnek 3: "men" ve "women" birbirinin anagramı değildir.
print(anagram("men", "women"))  # False

# Örnek 4: "listen" ve "silent" birbirinin anagramıdır.
print(anagram("listen", "silent"))  # True

# Örnek 5: "rail safety" ve "fairy tales" birbirinin anagramıdır.
print(anagram("rail safety", "fairy tales"))  # True
