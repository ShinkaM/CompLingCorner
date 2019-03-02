# Author: Shinka Mori
from array import *
import sys
from  collections import defaultdict
input = []
str = ''

#reads in file
print(sys.argv[1])
file_name = sys.argv[1]

f = open(file_name)
data = f.readlines()
f.close()

num = int(data[0])
print(num)

text = "".join(data[1: len(data)-num]).split()#gets the text, split it by line
acronym = "".join(data[len(data)-num: len(data)]).splitlines()#gets the acronyms. splits it by line

#print statements to show the text and acronym
for i in text:
    print(i)

for a in acronym:
    print(a)
    for c in range(len(a)):

        print(a[c])
'''
sets up the initial dict of acronyms, used to keep track of the order & completion of the expanded acronym list. tag unexpaned acronym with <UNK>
'''
def data_prep(acronym):
    dict = {}
    for a in acronym:
        dict[a] = '<UNK>'
    
    for v in dict:
        degree_identifier(v, dict)
        abnormal_identifier(v, dict)
    return dict

def acro_expander(text, acronym, dict):
    skip = ["and", "of", "at", "for"]#words not typically included in acronym; disregarded when expanded

    for acro in acronym:#for each looping for acronyms
        for char in range(len(acro)):#for looping for each character in acronym
            is_acro = False
            expanded = []
            for word in text:#for each looping for each word in text
                for s in skip:#for each word in words to skip/check
                    # check that the acronm's character is the first character of the word, and that the word le gth is more than 1
                    if is_acro and word.lower == s and char < len(acro):# the word matches a skip word
                        expanded.append(s)
                        continue
                    else:# the word is not a skip word

                        if acro[char] == word[0] and len(word) > 1:
                            expanded.append(word)
                            is_acro = True
                            char+=1
                        else:
                            is_acro = False

                            if(char == len(acro) and is_acro):#append the expanded acronym to ret
                                dict[acro] = expanded
                                break
    return dict
'''
don't know what the best way to identiy abnormal acronym is, currently solved by detecting them beforehand
'''
def degree_identifier(text, dict):
    if text == 'LLD':
        dict['LLD'] = 'Doctor of Law'
    elif text == 'LLB':
        dict['LLB'] = 'Bachelor of Law'
def abnormal_identifier(text, dict):
    if text == 'INTELSAT':
        dict['INTELSAT'] = 'International Telecommunication Satellite'
    elif text == 'UNICEF'
        dict['UNICEF'] = 'United Nations Children\'s Fund'


#Current problems: expanding UNICEF
