from collections import OrderedDict

def read_fasta(filen):

    d = OrderedDict()

    d2 = OrderedDict()

    with open(filen) as file:

        lst = file.readlines()

    i = 0

    ID = ''

    while i < len(lst):

        if lst[i][:1] == '>':

            ID = lst[i][1:-1]

            d[ID] = []

            i += 1

        else:

            d[ID].append(lst[i].strip('\n'))

            i += 1

    for i in d:

        d[i] = ''.join(d[i])

        d2[i] = (d[i].count('C') + d[i].count('G'))/(len(d[i]))*100

    return d


def binarySearch():

    with open('rosalind_bins.txt') as file:

        n = int(file.readline())

        m = int(file.readline())

        lst = list(map(int, file.readline().split()))

        tgt = list(map(int, file.readline().split()))

    rslt = []



    def find(lst, k):

        lower, upper = 0, len(lst) - 1

        while lower <= upper:

            middle = (lower + upper) // 2

            if lst[middle] == k:

                return middle + 1



            elif lst[middle] < k:

                lower = middle + 1

            else:

                upper = middle - 1

        return -1

    for k in tgt:

        rslt.append(find(lst, k))

    print(*rslt)





def merge_sort(arr):

    if len(arr) > 1:

        mid = len(arr) // 2

        lefthalf = arr[:mid]

        righthalf = arr[mid:]



        merge_sort(lefthalf)

        merge_sort(righthalf)



        i = 0

        j = 0

        k = 0

        while i < len(lefthalf) and j < len(righthalf):

            if lefthalf[i] < righthalf[j]:

                arr[k] = lefthalf[i]

                i = i+1

            else:

                arr[k] = righthalf[j]

                j = j+1

            k = k+1



        while i < len(lefthalf):

            arr[k] = lefthalf[i]

            i = i+1

            k = k+1



        while j < len(righthalf):

            arr[k] = righthalf[j]

            j = j+1

            k = k+1

    return arr

def SharedSplicedMotif():

    d = read_fasta('rosalind_lcsq.txt')

    print(d)

    ids = [_ for _ in d]

    lts = []

    for id in ids:

        lts.append(d[id])

    print(lts)



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



    spliced_motif = ''

    x, y = len(s), len(t)

    while x * y != 0:

        if lengths[x][y] == lengths[x - 1][y]:

            x -= 1

        elif lengths[x][y] == lengths[x][y - 1]:

            y -= 1

        else:

            spliced_motif = s[x - 1] + spliced_motif

            x -= 1

            y -= 1

    print(spliced_motif)

def reshape(l, n):

    return zip(*[iter(l)] * n)

def translatingRNAtoProtein(dna):  ## rosalind_prot.txt

    prot = ''

    d = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',

        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',

        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',

        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',

        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',

        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',

        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',

        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',

        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',

        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',

        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',

        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',

        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',

        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',

        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',

        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}



    ##with open(file) as file:

    ##    for line in file:

    ##        rna += line.strip('\n')



    for i in range(0, len(dna), 3):

        if d[dna[i:i+3]] != '_':

            prot += d[dna[i:i+3]]

        else:

            break

    return prot



