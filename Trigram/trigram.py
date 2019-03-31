" get input, split by sentence.  Break each sentence into individual words. Make a dictionary(key = trigram, value = count of trigram), and return the most frequent trigram; if there is none return the first trigram."


#!/bin/python3

import math
import os
import random
import re
import sys




s = "I love to dance. I like to dance I. like to play chess."
sentences = s.split(".")
print(sentences)
#
#sentences[0].split('.')
#sentences[1].split('.')
#sentences[2].split('.')

trigrams = {}
for sen in sentences:
    words = sen.split()
    for i in range(0, len(words) - 3):
        trigram_word = " ".join(words[i:i+3])
        if trigram_word not in trigrams:
            trigrams[trigram_word] = 1
        else:
            trigrams[trigram_word] += 1

print(trigrams)
output =max(trigrams, key = trigrams.get)
print(output.lower())


