def solution(genres, plays):
    answer = []
    sum_dict = {}
    play_dict = {}
    gen_list = list(set(genres))
    sum_list = [(0,0,0) for i in range(len(gen_list))]
    
    
    for i in range(len(genres)):
        gen = genres[i]
        p = plays[i]
        idx = gen_list.index(gen)
        new = (sum_list[idx][0]+p, gen)
        sum_list[idx] = new
        # sum_list[idx] += p
        
        if (gen in sum_dict):
            sum_dict[gen] += p
        else:
            sum_dict[gen] = p
        if (gen in play_dict):
            play_dict[gen].append((p,i))
        else:
            play_dict[gen] = [(p,i)]
    # print(sum_list)
    # print(play_dict)
    
    sum_list.sort(key=lambda x: (-x[0]))
    for s in sum_list:
        gen = s[1]
        play_list = play_dict[gen]
        play_list.sort(key=lambda x: (-x[0]))
        for i in range(len(play_list)):
            if (i < 2):
                answer.append(play_list[i][1])
            else:
                break
        
    return answer