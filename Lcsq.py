from Utils import read_fasta
#here i used a function called read_fasta to open and analyze the fasta-format dataset

def SharedSplicedMotif(d):

    ids = [_ for _ in d]

    lts = []

    for id in ids:

        lts.append(d[id])

    lts.sort(key=len)

    s = lts[0]

    t = lts[1]

    lengths = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

    for i, x in enumerate(s):

        for j, y in enumerate(t):

            if x == y:

                lengths[i + 1][j + 1] = lengths[i][j] + 1

            else:

                lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])

    motif = ''

    x, y = len(s), len(t)

    while x * y != 0:

        if lengths[x][y] == lengths[x - 1][y]:

            x -= 1

        elif lengths[x][y] == lengths[x][y - 1]:

            y -= 1

        else:

            motif = s[x - 1] + motif

            x -= 1

            y -= 1

    print(motif)





if __name__ == '__main__':

    d = read_fasta('rosalind_lcsq.txt')

    SharedSplicedMotif(d)