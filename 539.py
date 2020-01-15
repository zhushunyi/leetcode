class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        #time exceed
        '''mini = 1440
        for i in range(0,len(timePoints)):
            if i in timePoints[i+1:]:
                return 0
            for j in range(i+1,len(timePoints)):
                hour1 = timePoints[i][0:2]
                minute1 = timePoints[i][3:]
                hour2 = timePoints[j][:2]
                minute2 = timePoints[j][3:]
                time1 = int(hour1) * 60 + int(minute1)
                time2 = int(hour2) * 60 + int(minute2)
                diff = abs(time1 - time2)
                if diff >= 720:
                    diff = 1440 - diff
                mini = min(mini,diff)
        return mini'''
        time = []
        for i in timePoints:
            hour = i[:2]
            minute = i[3:]
            new_time = int(hour)*60 + int(minute)
            time.append(new_time)
        time.sort()
        print(time)
        #special case, compare the last and the first
        mini = time[-1] - time[0]
        if mini >=720:
            mini = 1440 - mini
        for i in range(1,len(time)):
            temp = abs(time[i] - time[i-1])
            if temp >=720:
                temp = 1440-temp
            print(temp)
            mini = min(mini,temp)
        return mini