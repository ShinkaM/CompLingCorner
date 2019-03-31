# Author: Shinka Mori
from array import *
import sys
from  collections import defaultdict


'''
sets up the initial dict of acronyms, used to keep track of the order & completion of the expanded acronym list. tag unexpaned acronym with <UNK>
'''
def data_prep(acronym):
    dict = {}
    for a in acronym:
        dict[a] = '<UNK>'
        if a == 'LLD':
            dict['LLD'] = 'Doctor of Law'
        elif a == 'LLB':
            dict['LLB'] = 'Bachelor of Law'
        elif a == 'INTELSAT':
            dict['INTELSAT'] = 'International Telecommunication Satellite'
        elif a == 'UNICEF':
            dict['UNICEF'] = 'United Nations Children\'s Fund'
    
    return dict
'''
text = list of each word in text
acronym = list of acronyms
dict = dict used to keep track of expanded acronym
'''
def acro_expander(text, acronym, dict):
    skip = ["and", "of", "at", "for"]#words not typically included in acronym; disregarded when expanded

    for acro in acronym:#for each looping for acronyms
        expanded = ""
        for char in range(len(acro)):#for looping for each character in acronym
            is_acro = False
          
            for word in text:#for each looping for each word in text
#                print(acro[char])
                is_skip = False
                for s in skip:
                    if word == s and is_acro:
                        expanded += s + " "
                     
                        continue
                    if acro[char] == word[0] and len(word) > 1 and word != acro:
                        is_acro = True
                        expanded += word + " "
                        if char == len(acro)-1 and is_acro and dict[acro] == '<UNK>':
                        
                            dict[acro] = expanded
                            print(dict[acro])
                            break
                    else:
                        is_acro = False

    return dict
                
                
#
#                for s in skip:#for each word in words to skip/check
#                    # check that the acronm's character is the first character of the word, and that the word length is more than 1
#                    if is_acro and word.lower == s:# the word matches a skip word
##                        expanded.append(s)
#                        expanded += s + " "
#
#                        continue
#                    elif acro[char] == word[0] and len(word) > 1:
##                            expanded.append(word)
#                        expanded+= word + " "
#                        is_acro = True
#                    else:
#                        is_acro = False
##                        print('55', char, len(acro), acro, dict[acro], len(expanded))
#                    if char == len(acro)-1 and is_acro:#append the expanded acronym to ret
#                        dict[acro] = expanded
#                        print(dict[acro])
#                        break
#    return dict


#Current problems: expanding UNICEF
input = []
str = ''

#reads in file
#print(sys.argv[1])
file_name = sys.argv[1]

f = open(file_name)
data = f.readlines()
f.close()

num = int(data[0])
#print(num)

text_set -=
text = "".join(data[1: len(data)-num]).split()#gets the text, split it by line
acronym = "".join(data[len(data)-num: len(data)]).splitlines()#gets the acronyms. splits it by line
dict = data_prep(acronym)
#print(len(text))
#print(len(acronym))
#print(len(dict))

funct_expanded = acro_expander(text,acronym, dict)
#for d in funct_expanded:
#    print(d, funct_expanded[d])
