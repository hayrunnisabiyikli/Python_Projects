def palindrome(sentence):
    for i in (",.'?/><}{{}}'"):
        sentence = sentence.replace(i, "")  # Noktalama işaretleri kaldırılıyor
    palindrome = []  # Palindrom kelimelerin tutulacağı boş bir liste oluşturuluyor
    words = sentence.split(' ')  # Cümle kelimelere ayrılıyor
    for word in words:
        word = word.lower()  # Kelime küçük harflere dönüştürülüyor
        if word == word[::-1]:  # Kelime ters çevrildiğinde kendisiyle aynıysa (palindromsa)
            palindrome.append(word)  # Palindrom listesine ekleniyor
    return palindrome  # Palindrom kelimelerin listesi döndürülüyor

sentence = input("Enter a sentence: ")
print(palindrome(sentence))  # sentence = LOL, My interview went good. My Mom will be so happy.
