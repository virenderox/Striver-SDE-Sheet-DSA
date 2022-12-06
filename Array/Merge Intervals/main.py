class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        merge = []
        intervals.sort()

        n = len(intervals)
        compare = intervals[0]
        take = 1
        while take <= n-1:

            compareArr = intervals[take]

            if compare[1] >= compareArr[0]:
                compare = [min(compare[0],compareArr[0]), max(compare[1],compareArr[1])]

            else:
                merge.append(compare)
                compare = compareArr

            take += 1
        merge.append(compare)

        return  merge

        
