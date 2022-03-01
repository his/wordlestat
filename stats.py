import re

f = open("words.js","r")

for x in f:
    words = re.findall(r'([a-z]{5})',x)

words_with_doubles = []
words_with_double_sequence = []

regexp = re.compile(r"(.)\1")

for w in words:
    match = re.search(regexp,w)
    if match:
        words_with_double_sequence.append(w)
    sorted_w = "".join(sorted(w))
    match = re.search(regexp,sorted_w)
    if match:
        words_with_doubles.append(w)

print ("Words with double letters in sequence: ", len(words_with_double_sequence), " out of ", len(words))
print ("Words with double letters anywhere: ", len(words_with_doubles), " out of ", len(words))
