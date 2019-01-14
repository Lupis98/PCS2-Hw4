import itertools
#define n
n = 6

p = list(itertools.permutations([i for i in range(1, n + 1)]))

print (len(p))

for pm in p:

    print (str(pm)[1:].replace(')', '').replace(',', ''))