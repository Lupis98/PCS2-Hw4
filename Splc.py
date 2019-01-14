from Utils import read_fasta, translatingRNAtoProtein

def rnaSplicing(d):

    id = [_ for _ in d]

    ss = id[0]

    for i in id[1:]:

        if d[i] in d[ss]:

            d[ss] = d[ss].replace(d[i], '')

        else:

            print('not sub')

    print(translatingRNAtoProtein(d[ss]))


if __name__ == '__main__':

    d = read_fasta('rosalind_splc.txt')

    print(rnaSplicing(d))