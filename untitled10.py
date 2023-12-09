

from google.colab import drive
drive.mount('/content/drive')

text = ('https://drive.google.com/file/d/1cpsgB75_sTG4y99-ERCag_NYjcIbPaiZ/view?usp=drive_link')

from collections import Counter
from functools import reduce

def most_frequent_word(test_list):
	all_words = reduce(lambda a, b: a + b, [sub.split() for sub in test_list])
	word_counts = Counter(all_words)
	return word_counts.most_common(1)[0][0]

test_list = ["какать какать как какать"]
print("most of chasto use word: ", most_frequent_word(test_list))

#должен быть текст войны и мира и вывод какать