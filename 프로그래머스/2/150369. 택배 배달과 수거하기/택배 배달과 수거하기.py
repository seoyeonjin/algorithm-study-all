def solution(cap, n, deliveries, pickups):
    answer = 0
    # i = n -1

    d_idx = n - 1  # 배달용 포인터
    p_idx = n - 1  # 수거용 포인터
    
    while d_idx >= 0 or p_idx >= 0:
        while d_idx >= 0 and deliveries[d_idx] == 0:
            d_idx -= 1
        while p_idx >= 0 and pickups[p_idx] == 0:
            p_idx -= 1

        if d_idx < 0 and p_idx < 0:
            break
            
        farthest = max(d_idx, p_idx) + 1
        answer += farthest * 2

        ccap = cap
        dindex = d_idx
        while ccap and dindex >= 0:
            # print(ccap, dindex, deliveries[dindex])
            if (ccap >= deliveries[dindex]):
                ccap -= deliveries[dindex]
                deliveries[dindex] = 0
                dindex -= 1
            else:
                deliveries[dindex] -= ccap
                ccap = 0
                dindex -= 1
        pindex = p_idx
        pcap = cap
        while pcap and pindex >= 0:
            if (pcap >= pickups[pindex]):
                pcap -= pickups[pindex]
                pickups[pindex] = 0
                pindex -= 1
            else:
                pickups[pindex] -= pcap
                pcap = 0
                pindex -= 1
    return answer