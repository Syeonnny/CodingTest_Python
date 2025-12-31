words = input() 
corpus = []
for i in range(1, len(words)-1): 
    for j in range(i+1, len(words)):
        one = ''.join(reversed(words[0:i]))
        two = ''.join(reversed(words[i:j]))
        three = ''.join(reversed(words[j:]))

        corpus.append(one + two + three)
print(sorted(corpus)[0])