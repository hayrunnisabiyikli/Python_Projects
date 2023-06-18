def recursive_binary_search(target, sequence, first, last):
    # İndekslerin geçersiz olduğu durumda False döndürülür
    if first > last:
        return False
    else:
        # Orta noktanın indeksini bulmak için ilk ve son indekslerin ortalaması alınır
        mid = (last + first) // 2

        # Orta noktadaki değer hedef değere eşitse True döndürülür
        if sequence[mid] == target:
            return True

        # Hedef değer orta noktadan küçükse aramanın sol yarısında devam edilir
        elif target < sequence[mid]:
            return recursive_binary_search(target, sequence, first, mid - 1)

        # Hedef değer orta noktadan büyükse aramanın sağ yarısında devam edilir
        else:
            return recursive_binary_search(target, sequence, mid + 1, last)


# Örnek kullanım
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_number = 13

# Fonksiyonu kullanarak hedef değeri arama
result = recursive_binary_search(target_number, numbers, 0, len(numbers) - 1)

# Sonucu ekrana yazdırma
print(result)  # True