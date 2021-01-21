def MergeIntervals(intervals) :
    intervals.sort()
    result=[]
    curr=intervals[0]

    for next in intervals:
        if max(curr)>=min(next):
            curr=[curr[0],max(curr[1],next[1])]
        else:
            result.append(curr)
            curr=next
            
    result.append(curr)

    return result


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(MergeIntervals(intervals))   