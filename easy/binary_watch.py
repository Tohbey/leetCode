class Solution:
    from collections import defaultdict
    
    def __init__(self):
        
        self.hours = defaultdict(list)
        self.minutes = defaultdict(list)
        
        for i in range(60):
            
            if i < 12:
                self.hours[bin(i).count('1')].append(i)
            self.minutes[bin(i).count('1')].append(i)
        
        print(self.minutes)
        
        return None
        
        
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        times = []
        
        for h in range(min(4, turnedOn)+1):
#            print(h, self.minutes[turnedOn-h])
            if self.minutes[turnedOn-h]:
                times.extend([str(hour) + ':' + str(minute).rjust(2, '0') for hour in self.hours[h] for minute in self.minutes[turnedOn-h]])
        
        return times
        