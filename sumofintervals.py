def sum_of_intervals(intervals):
    totallst = []
    for x in intervals:
        for i in range(x[0],x[1]):
            totallst.append(i)
    totallst = list(set(totallst))
    totallst.sort()
    return len(totallst)



print(sum_of_intervals([(1, 5), (1, 5)]))