def get_alphabetCount(word, alphabet):
    count = 0
    for i in word:
        if i == alphabet:
            count += 1
    return count

word = input()
word = word.upper()

used_alphabets = []
for i in word:
    if i not in used_alphabets:
        used_alphabets.append(i)

maxCount = 1
maxAlphabet = "?"
for i in used_alphabets:
    if maxCount > get_alphabetCount(word, i):
        maxCount = get_alphabetCount(word, i)
        maxAlphabet = i
    if maxCount == get_alphabetCount(word, i):
        maxAlphabet = "?"

if list(word).count == 1:
    maxAlphabet = word
print(maxAlphabet)
        
