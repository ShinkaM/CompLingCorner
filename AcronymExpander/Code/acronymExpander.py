# Author: Nick Bellizzi
'''
    text = text put, acronym = list of acronyms
    note that this assumes that the acronym appears in the text
'''
def expand(text, acronym):
    words = text.split() #splits inout by whitespace
    for i in range(len(words)):
        if acronym in words[i]: #tag the acronym to ignore acronyms
            words[i] = '(ignore)'
    start = end = -1
    for i in range(len(words)):
        if words[i][0] == acronym[0]:  # fix?? this starts to track the first index of the expanded acronym
            start = i
        elif start != -1 and words[i][0] == acronym[len(acronym) - 1]:#this tracks the last index of the acronym and breaks
            end = i
            break
    expanded = []
    for i in range(start, end + 1) :
        expanded.append(words[i])#for words in between the start and end acronmy characters, append them
    return ' '.join(expanded)

#have a list w the same size as num acro, check if it appears in the (), set a certain index of match sentence to the expanded acronym in (). otherwise go through list again, assign to remaining
num_inputs = int(input())
sentences = []
acronyms = []
for i in range(num_inputs):
    sentences.append(input())

for i in range(num_inputs):
    acronyms.append(input())

matched_sentences = []
for a in acronyms:
    for sen in sentences :
        # acroParen = '(' + a + ')'
        if a in sen :
            matched_sentences.append(sen)
            break

for i in range(num_inputs):
    print(expand(matched_sentences[i], acronyms[i]))

