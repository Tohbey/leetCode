class Solution:
    def getEntries(n, queries):
        ans = []
 
        goodArray = Solution.getGoodArray(n);
        
        for query in queries:
           l = query[0]
           r = query[1]
           print(l, r)
           if(l == r):
               if(len(goodArray) < len(query)):
                   result = goodArray[l-1]
               else:
                   result = goodArray[l]
           else:
               if(len(goodArray) < len(query)):
                   result = goodArray[l-1] * goodArray[r-1]
               else:
                   result = goodArray[l] * goodArray[r]
           print(result % query[2])           
        print(ans)
        
    def getGoodArray(n):
        v = []
        goodArray = []
        
        while n > 0:
            v.append(int(n % 2))
            n = int(n/2)
        for i in range(0, len(v)):
            if (v[i] == 1):
                goodArray.append(2**i)