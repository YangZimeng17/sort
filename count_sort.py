#counting sort
#O(n)

def count_sort(L):
    '''L, list of non-negative integer'''

    #find max int of L
    max = 0
    for n in L:
        if n > max:
            max = n

    #count the frequency of element in L
    count = [0 for i in range(max + 1)]
    for i in range(len(L)):
        count[L[i]] += 1

    #rearrage index for each integer in L
    total = 0
    for i in range(max + 1):
        count[i], total = total, count[i] + total

    #sorted list
    output = [0 for i in range(len(L))]
    for i in range(len(L)):
        output[count[L[i]]] = L[i]
        count[L[i]] += 1

    return output

test = [[2,3,1,5,5,7,0,0]]

for e in test:
    print(count_sort(e))


