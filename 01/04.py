# from langdetect import detect
import langdetect


text_1 = "War doesn't show who's right, just who's left."
text_2 = "Ein, zwei, drei, vier"

print(langdetect.detect(text_1))
print(langdetect.detect(text_2))

print("Hello, world")
