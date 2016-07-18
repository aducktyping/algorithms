
def merge_and_count_split_inversions(a, b):
    c = []
    inversions = 0
    i = 0
    j = 0
    while((i < len(a)) and (j < len(b))):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += len(a) - i
    if (i < len(a)):
        c.extend(a[i:])
    else:
        c.extend(b[j:])
    return inversions, c

def sort_and_count_inversions(a):
    n = len(a)
    if n == 1: 
        return 0, a
    else:
        half = int(n/2)
        x, b = sort_and_count_inversions(a[:half])
        y, c = sort_and_count_inversions(a[half:])
        z, d = merge_and_count_split_inversions(b, c)
    return (x+y+z), d

def count_inversions(a):
    count, _ = sort_and_count_inversions(a)
    return count

if __name__ == '__main__':
    with open(r'./IntegerArray.txt', 'r') as f:
        data = f.read()
    a = [int(x) for x in data.strip().split('\n')]
    count = count_inversions(a)
    print(count)