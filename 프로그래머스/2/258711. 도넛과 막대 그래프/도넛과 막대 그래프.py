def solution(edges):
    answer = []
    node = [[0,0] for i in range(1000001)] # 초기화
    # 각 노드별 들어오는 거, 나가는 거
    
    start = -1
    for e in edges:
        a,b= e
        node[a][1] += 1
        node[b][0] += 1
    # 나가는 점이 2개 이상 있는 데 들어오는 점은 없는 점 -> 생성한 정점
    # 나가는 화살표의 개수가 전체 모양의 개수다 ! 
    for i in range(len(node)):
        n = node[i]
        if (n[0] == 0 and n[1] >= 2): 
            start = i
    total_cnt = node[start][1]
    # print("total_cnt: ", total_cnt)
    
    # print(node)
    bar_cnt = 0
    for e in edges:
        a,b = e
        if (a == start):
            node[b][0] -= 1
            if (node[b][0] == 0 and node[b][1] == 0):
                bar_cnt += 1
    
    # 8자 모양 그래프의 개수는? 
    eight_cnt = 0
    for n in node:
        if (n[0] == 2 and n[1] == 2): 
            eight_cnt += 1
    
    # 막대 모양 그래프의 개수는? 
    
    for n in node:
        if (n[0] == 0 and n[1] == 1): 
            bar_cnt += 1
    
    donut_cnt = total_cnt - eight_cnt - bar_cnt
    answer = [start, donut_cnt, bar_cnt, eight_cnt]
    # print(node)
   
    return answer