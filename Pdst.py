seq_lst = []

sts = ''

for l in open('rosalind_pdst.txt'):

    if l[0] == '>':

        if sts != '':

            seq_lst.append(sts)

            sts = ''

    else:

        sts = sts + l.strip('\n')

seq_lst.append(sts)

dis_m = []

tmp_m = []

n = len(sts)

for i in range(len(seq_lst)):

    for j in range(len(seq_lst)):

        dis = 0.0

        for k in range(n):

            if seq_lst[i][k] != seq_lst[j][k]:

                dis += 1

        tmp_m.append(dis / n)

    dis_m.append(tmp_m)

    tmp_m = []





for x in dis_m:

    print(' '.join([str(m) for m in x]))