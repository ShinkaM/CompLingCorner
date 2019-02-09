# Author: Nick Bellizzi
def expand(text, acronym):
    words = text.split()
    for i in range(len(words)):
        if acronym in words[i]:
            words[i] = '(ignore)'
    start = end = -1
    for i in range(len(words)):
        if words[i][0] == acronym[0]:  # fix??
            start = i
        elif start != -1 and words[i][0] == acronym[len(acronym) - 1]:
            end = i
            break
    expanded = []
    for i in range(start, end + 1) :
        expanded.append(words[i])
    return ' '.join(expanded)


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

