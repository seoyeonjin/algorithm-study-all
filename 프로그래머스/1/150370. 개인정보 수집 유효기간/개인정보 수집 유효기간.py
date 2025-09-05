def solution(today, terms, privacies):
    answer = []
    for i in range(len(privacies)):
        p = privacies[i]
        sd, plan = p.split(" ")
        year, month, day = sd.split(".")
        for t in terms:
            tp, tm = t.split(" ")
            if (plan == tp):
                intmonth = int(month)
                m , d = divmod(int(tm), 12)
                year = str(int(year) + m)
                aftermonth = intmonth + d
                if (aftermonth > 12):
                    aftermonth -= 12
                    year = str(int(year) + 1)
        if (day == "01"):
            aftermonth -= 1
            if (aftermonth == 0):
                aftermonth = 12
                year = str(int(year) - 1)
            day = "28"
        else:
            day = str(int(day) - 1)
        year = int(year)
        day = int(day)
        print(year, aftermonth, day)
        tyear, tmonth, tday = map(int, today.split("."))
        if (tyear > year):
            answer.append(i+1)
        elif (tyear == year):
            if (tmonth > aftermonth):
                answer.append(i+1)
            elif (tmonth == aftermonth):
                if (tday > day):
                    answer.append(i+1)
    return answer