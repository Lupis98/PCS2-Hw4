#define s,t
s = 'ACTTCCCTCGCCACTTCCCGCGAAACTTCCCCCACTTCCCACTTCCCGACTTCCCCGGGACTTCCCACTTCCCACTTCCCAACTTCCCACTTCCCTCTACTTCCCTATGGGGGAGTCGACTTCCCACTTCCCACTTCCCAAACTTCCCTACTTCCCCAACTTCCCACTTCCCACTTCCCGGGCGACTTCCCCTTACTTCCCGACTTCCCTGCAGAAGTAGACCGCTGACGCGACTTCCCATGGCAGCACTTCCCAGACTTCCCACAAAACTTCCCTGCCACTTCCCTATAGACTCAAACTTCCCGGAGGAGGACTTCCCCACTTCCCATGGATCACTTCCCGTCAAAACTTCCCTACTTAGTAGGACTTCCCTACTTCCCTCCACTTCCCAACTTCCCCTACTTCCCTAAACTTCCCGACTTCCCCACTTCCCACTTCCCTACTTCCCTAATATACTTCCCTACTTCCCACTTCCCAATACTTCCCTCTTTACTTCCCCTACTTCCCTACTTCCCCATCGCACTTCCCCAACTTCCCTAACACTTCCCTCAGGACTTCCCACTTCCCTATTACTTCCCACAGTGCACTTCCCAACTTCCCAGACTTCCCACACTTCCCAACTTCCCGGGCACTTCCCTTGAAGGATTGTACTTCCCTACTTCCCGTACTTCCCACTTCCCCAAGACGCACACTTCCCTACTTCCCTCCTGCACTTCCCCACTTCCCATCCCATGTTTACTTCCCCAACTTCCCACTTCCCGTTAACTGACTTCCCGGCCGGGATGAGACTACTTCCCCACTTCCCAACTTCCCCCCGACTTCCCGCCAATTTGCTACTTCCCCAACTTCCCCAACTTCCC'

t = 'ACTTCCCAC'

ind = []

for i in range(len(s)-len(t)+1):

    if s[i:i+len(t)] == t:

        ind.append(i+1)

for i in ind:

    print (i)