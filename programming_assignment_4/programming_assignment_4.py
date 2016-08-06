from collections import defaultdict, Counter

def pass_1(G, n):
    '''First DFS pass of the Kosaraju algorithm. Takes a graph (G) in adjacent 
    list form, reverses it, and computes the finishing times of each vertex in
    a depth-first search. The DFS uses a non-recursive algorithm.'''
    G_rev = defaultdict(lambda: [])
    for u, vs in G.items():
        for v in vs:
            G_rev[v].append(u)
    t = 0
    explored = defaultdict(lambda: False)
    f_times = {}
    for i in range(n, 0, -1):
        if explored[i]:
            continue
        u = i
        visited = defaultdict(lambda: False)
        trail = []
        while True:
            visited[u] = True
            try:
                v = next(v for v in G_rev[u] if (not explored[v]) and (not visited[v]))
            except StopIteration:
                explored[u] = True
                t += 1
                f_times[u] = t
                try:
                    u = trail.pop()
                except IndexError:
                    break
            else:
                trail.append(u)
                u = v

    return f_times

def pass_2(G, n, f_times):
    '''Second DFS pass of the Kosaraju algorithm. Takes a graph (G) in adjacent 
    list form, and computes the finishing times of each vertex starting with the
    highest numbered finishing time from the first pass and continuing down.
    The DFS uses a non-recursive algorithm.'''
    order = {v: k for k, v in f_times.items()}
    explored = defaultdict(lambda: False)
    leaders = {}
    for i in range(n, 0, -1):
        s = i
        u = order[i]
        if explored[u]:
            continue
        visited = defaultdict(lambda: False)
        trail = []
        while True:
            visited[u] = True
            leaders[u] = s
            try:
                v = next(v for v in G[u] if (not explored[v]) and (not visited[v]))
            except StopIteration:
                explored[u] = True
                try:
                    u = trail.pop()
                except IndexError:
                    break
            else:
                trail.append(u)
                u = v

    return leaders

def kosaraju(G):
    '''Takes a graph in adjacent list form and computes the SCC "leaders" and their respective sizes'''
    n = 0
    for u, vs in G.items():
        if u > n: 
            n = u
        for v in vs:
            if v > n:
                n = v
            
    f_times = pass_1(G, n)
    leaders = pass_2(G, n, f_times)
    
    return leaders

if __name__ == '__main__':
    G = defaultdict(lambda: [])
    with open(r'./SCC.txt', 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        u, v = (int(x) for x in line.strip().split())
        G[u].append(v)
        
    leaders = kosaraju(G)
    counts = Counter(leaders.values())
    top_5 = list(zip(*counts.most_common()))[1][:5]
    print(",".join(str(i) for i in top_5))                      # outputs "434821,968,459,313,211"