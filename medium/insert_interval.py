from pip import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda i : i[0]) 
        
        output = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = output[-1][1] 
            
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        
        print(output)
        return output
    
res = Solution()

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] 
newInterval = [4,8]
res.insert(intervals, newInterval)