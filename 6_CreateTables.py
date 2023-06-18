from tabulate import tabulate

data = [["Name", "Place", "Gender"], ["Aman", "New Delhi", "Male"], ["Hritika", "New Delhi", "Female"], ["Krishna", "UP", "Male"]]

# Tabulate modülünü kullanarak verileri tablo formatında yazdırıyoruz
table = tabulate(data)

# Tabloyu ekrana yazdırıyoruz
print(table)
