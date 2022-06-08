"""Note I just wrote this here and haven't tested it, but it is something like this!"""

from collections import defaultdict

def topo_sort_BFS(graph):
    #
    # calc in degree of each node
    in_degrees = defaultdict(int)
    for node1 in graph.keys():
        in_degrees[node1]
        for node2 in graph[node1]:
            in_degrees[node2] += 1
    print(in_degrees)
    #
    # initialize q with all 0 in degree nodes
    visited = set() # this is only used later on so we could just say if in_degrees[nei] == 0 (already) then we know it's 'visited'
    q = deque()
    for key in in_degrees:
        if in_degrees[key] == 0:
            q.append(key)
            visited.add(key)
    print(q)
    #
    # start bfs
    topo_sort = []
    while q:
        c = q.popleft()
        topo_sort.append(c)
        for nei in graph[c]:
            if nei not in visited:
                in_degrees[nei] -= 1
                if in_degrees[nei] == 0:
                    q.append(nei)
                    visited.add(nei)
    #
    return topo_sort
