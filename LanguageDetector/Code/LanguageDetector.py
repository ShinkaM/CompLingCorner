# Author: Nick Bellizzi

from collections import Counter
import re


def detect_language(sample_text):

    # Most frequent words in languages to detect
    english = ['the', 'was', 'to', 'of', 'and', 'that', 'is', 'i', 'it', 'with']
    french = ['je', 'est', 'pas', 'vous', 'va', 'il', 'ça', 'moi', 'nous', 'dans']
    german = ['ich', 'sie', 'ist', 'nicht', 'und', 'der', 'wir', 'zu', 'mir', 'auf']
    # spanish = ['el', 'lo', 'por', 'como', 'para', 'está', 'pero', 'yo', 'eso', 'aquí']

    # Remove punctuation with regular expression
    s = re.sub(r'[^\w\s]', '', sample_text)

    # Convert to uniform case
    s = s.lower()

    # Split text into list and get frequencies with counter
    words = s.split()
    frequencies = Counter(words)

    # Search through each language list
    for word in frequencies:
        for en in english:
            if word == en:
                return 'English'
        for fr in french:
            if word == fr:
                return 'French'
        for de in german:
            if word == de:
                return 'German'
        '''
        Not exactly necessary: if we're confident enough that the word
        isn't part of the first three languages, it must be Spanish.
        The biggest difference is that this means that though the remaining
        lists must be exhausted before returning a guess, we don't have to worry
        about Spanish words ever interfering with other languages.
        
        for es in spanish:
            if word == es:
                return 'Spanish'
        '''

    return 'Spanish'


if __name__ == '__main__':
    s = input()
    print(detect_language(s))
