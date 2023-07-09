from forex_python.converter import CurrencyRates  # forex_python.converter modülünden CurrencyRates sınıfını import et

c = CurrencyRates()  # CurrencyRates sınıfından bir örnek oluştur

amount = int(input("Enter the amount: "))  # Kullanıcıdan bir miktar girişi al

from_currency = input("From Currency: ").upper()  # Kaynak para birimini büyük harflere dönüştürerek al

to_currency = input("To Currency: ").upper()  # Hedef para birimini büyük harflere dönüştürerek al

print(from_currency, " To ", to_currency, amount)  # Kaynak ve hedef para birimini ve miktarı ekrana yazdır

result = c.convert(from_currency, to_currency, amount)  # Dönüşümü gerçekleştir ve sonucu al

print(result)  # Sonucu ekrana yazdır


# pycharm üzereinden terminale pip install forex-python yazarak modülü yükleyebilirsiniz