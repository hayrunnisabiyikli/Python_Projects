from textblob import TextBlob

words = ["Data Scence", "Machine Learning"]
corrected_words = []

for word in words:
    corrected_words.append(TextBlob(word).correct())

print("Wrong words:", words)
print("Corrected Words are:")
for corrected_word in corrected_words:
    print(corrected_word, end=" ")
