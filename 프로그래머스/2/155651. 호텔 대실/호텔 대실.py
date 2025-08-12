
def solution(book_time):
    answer = 0
    num_list = [0] * 2000
    
    start = [0,0]
    end = [0,0]
    for book in book_time:
        ns, ne = book
        a,b = ns.split(":")
        ab = int(a) * 60 + int(b)
        
        c,d = ne.split(":")
        hours = int(c)
        minutes = int(d) + 10
        if minutes >= 60:
            minutes -= 60
            hours += 1
        cd = hours * 60 + minutes
        
        print(ab, cd)
        
    
        for i in range(ab, cd):
            num_list[i] += 1
            
            
        answer = max(num_list)
        
     
    
    return answer