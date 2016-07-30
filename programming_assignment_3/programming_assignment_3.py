from random import sample
from math import log
from copy import deepcopy

def contract(graph):
    n = len(graph)
    while n > 2:
        u = sample(graph.keys(), 1)[0]    # pick node to collapse into
        v = sample(graph[u], 1)[0]        # pick node to eliminate
        for w in graph[v]:                # for all w in the set of nodes pointing to v...
            graph[w] = [x if x != v else u for x in graph[w]]    # ...change w's connections to v to u instead
        graph[u].extend(graph[v])         # collapse all of v's connections into u
        graph[u] = [y for y in graph[u] if y != u]    # eliminate all self-loops (also eliminates collapsed edge)
        del graph[v]                      # delete the collapsed node
        n -= 1
        
    return graph

def min_cut(graph):
    min_cut_size = float('inf')
    n = len(graph)
    for _ in range(int(n*log(n))):               # it's not n^2*log(n), but this is way more than enough
        sml_graph = contract(deepcopy(graph))
        cut_size = len(sml_graph.popitem()[1])
        if cut_size < min_cut_size:
            min_cut_size = cut_size

    return min_cut_size
       
if __name__ == '__main__':
    with open(r'./kargerMinCut.txt', 'r') as f:
        data = f.read()
    lines = data.strip().split('\n')
    graph = {}
    for line in lines:
        nodes = [int(e)-1 for e in line.strip().split('\t')]
        graph[nodes[0]] = nodes[1:]

    print(min_cut(graph))  # prints '17'