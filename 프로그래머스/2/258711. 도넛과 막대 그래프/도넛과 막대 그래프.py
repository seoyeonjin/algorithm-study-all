def solution(edges):
    max_node = max(max(a,b) for a,b in edges)
    in_out = [[0,0] for _ in range(max_node+1)]
    
    for a,b in edges:
        in_out[a][1] += 1
        in_out[b][0] += 1
    
    if len(edges) == 1 and edges[0][0] == edges[0][1]:
        return [edges[0][0], 1, 0, 0]

    bar_count   = sum(1 for i,o in in_out if i >= 1 and o == 0)
    eight_count = sum(1 for i,o in in_out if i >= 2 and o >= 2)

    start_node = -1
    max_out = -1
    for k,(i,o) in enumerate(in_out):
        if i == 0 and o >= 2:
            start_node, max_out = k, o
            break
    
    donut_count = max_out - bar_count - eight_count
    return [start_node, donut_count, bar_count, eight_count]
