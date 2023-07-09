import matplotlib.pyplot as plt  # matplotlib.pyplot modülünü import et

x = [3, 5, 7, 8, 4]
y = [5, 3, 7, 8, 2]

plt.scatter(x, y)  # scatter plot grafiği çizdir

plt.show()  # grafiği ekranda göster

x = [3, 5, 7, 8, 4]
y = [5, 3, 7, 8, 2]
labels = ["Jan", "Feb", "Mar", "April", "May"]

plt.scatter(x, y)  # scatter plot grafiği çizdir

for i, j in enumerate(labels):
    plt.annotate(j, (x[i]+0.10, y[i]), fontsize=10)  # noktalara etiketleri ekle

plt.show()  # grafiği ekranda göster

# pycharm üzereinden terminale pip install matplotlib yazarak modülü yükleyebilirsiniz