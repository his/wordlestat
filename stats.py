import re

f = open("words.js","r")

for x in f:
    words = re.findall(r'([a-z]{5})',x)

words_with_doubles = []
words_with_double_sequence = []
words_with_double_vowels = []

regexp = re.compile(r"(.)\1")
regexvowel = re.compile(r"([aeiuo])\1")

for w in words:
    match = re.search(regexp,w)
    if match:
        words_with_double_sequence.append(w)
    sorted_w = "".join(sorted(w))
    match = re.search(regexp,sorted_w)
    if match:
        words_with_doubles.append(w)
        matchvow = re.search(regexvowel, sorted_w)
        if match:
            match = re.search(regexp, w)
            if not match:
                words_with_double_vowels.append(w)

print ("Words with double letters in sequence: ", len(words_with_double_sequence), " out of ", len(words))
print ("Words with double letters anywhere: ", len(words_with_doubles), " out of ", len(words))
print ("Words with double vowels: ", len(words_with_double_vowels), " out of ", len(words))
