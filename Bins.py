#I runned this function used also in the previous homework (PCS2-Hw3)
def binarySearch(file_name):

    with open(file_name) as file:

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

if __name__ == '__main__':

    file_name = 'rosalind_bins.txt'

    binarySearch(file_name)