import sys
sys.setrecursionlimit(10001)

def solution(nodeinfo):
    answer = []
    node_len = len(nodeinfo)
    
    for i in range(node_len):
        nodeinfo[i].append(i+1)
    
    nodeinfo.sort(key= lambda x: (-x[1], x[0]))
    
    post_result = []
    pre_result = []
    
    def make_order(node_list):
        right = []
        left = []
        if len(node_list) == 1:
            post_result.append(node_list[0][2])
            pre_result.append(node_list[0][2])
        elif (len(node_list) == 0):
            return
        else: 
            root = node_list[0]
            for i in range(len(node_list)):
                if (root[0] < node_list[i][0]):
                    right.append(node_list[i])
                elif (root[0] > node_list[i][0]):
                    left.append(node_list[i])

            right.sort(key= lambda x: (-x[1]))
            left.sort(key= lambda x: (-x[1]))

            pre_result.append(root[2])
            make_order(left)
            make_order(right)
            post_result.append(root[2])
        
    make_order(nodeinfo)
    
    answer.append(pre_result)
    answer.append(post_result)
        
    return answer