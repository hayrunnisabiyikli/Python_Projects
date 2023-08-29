import csv
import pandas as pd

# CSV dosyasını açma
with open('MoviesOnStreamingPlatforms_updated.csv', 'r') as file:
    reader = csv.reader(file)

    # Her satırı okuma
    for row in reader:
        print(row)


movies = pd.read_csv("MoviesOnStreamingPlatforms_updated.csv")

movies['Rotten Tomatoes'] = movies["Rotten Tomatoes"].str.replace("%", "").astype(float)
movies.drop("Type", inplace=True, axis=1)
correlations = movies.corr(method='pearson')
# Correlation Between All The Features
print(correlations)

# Correlation Between A Particular column "Year"
print(correlations["Year"])

# Visualizing Correlation
import seaborn as sns

import matplotlib.pyplot as plt
sns.heatmap(correlations)
plt.show()