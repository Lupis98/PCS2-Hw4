import sys
#I implemented the sys module for reading the fasta file,you insert the dataset.txt file in the command prompt as arg[1] of the sys method
def LCS(txt):

    for k in range(len(txt[0]), 1, -1):

        for start in range(len(txt[0]) - k + 1):

            c = txt[0][start:start + k]

            found = True

            for i in range(1, len(txt)):

                if not c in txt[i]:

                    found = False

                    break

            if found:

                return c



txt = [line.strip() for line in open(sys.argv[1])]

i = 2

while i < len(txt):

    if not txt[i].startswith('>') and not txt[i - 1].startswith('>'):

        txt[i - 1] += txt[i]

        del txt[i]

        i -= 1

    i += 1

i = 0

while i < len(txt):

    del txt[i]

    i += 1

print (LCS(txt))