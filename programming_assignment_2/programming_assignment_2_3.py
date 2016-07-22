import math

def partition(a):
    i = 1
    for j in range(1, len(a)):
        if a[j] > a[0]: continue
        else:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[0], a[i-1] = a[i-1], a[0]

    return a, i

def qs_comps_pivot_a_median(a):
    n = len(a)
    if n <= 1:
        return a, 0

    mid = math.ceil(n/2) - 1
    indices = 0, mid, -1
    candidates = [a[i] for i in indices]
    median = sorted(candidates)[1]
    idx = indices[candidates.index(median)]

    a[0], a[idx] = a[idx], a[0]
    
    a, i = partition(a)
    
    a[0:i-1], comps_l = qs_comps_pivot_a_median(a[0:i-1])
    a[i:], comps_r = qs_comps_pivot_a_median(a[i:])

    return a, comps_l + comps_r + (n - 1)
            
if __name__ == '__main__':
    with open(r'./QuickSort.txt', 'r') as f:
        data = f.read()
    a = [int(x) for x in data.strip().split('\n')]
    _, count = qs_comps_pivot_a_median(a)
    print(count)  # prints 138382