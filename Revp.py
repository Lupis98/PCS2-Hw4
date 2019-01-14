def revCompl( t ):

    rev = ''

    for c in t:

        if c == 'A':

            rev = 'T' + rev

        elif c == 'C':

            rev = 'G' + rev

        elif c == 'G':

            rev = 'C' + rev

        elif c == 'T':

            rev = 'A' + rev

    return rev



def RevPal( txt ):

    return txt == revCompl(txt)

#define dna

dna = 'TCAATGCATGCGGGTCTATATGCAT'

for l in range(4,13):

    for i in range(0,len(dna)-l+1):

        if RevPal(dna[i:i+l]):

            print (str(i+1) + ' ' + str(l))