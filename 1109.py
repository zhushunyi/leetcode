
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        #time exceed
        '''length = len(bookings)
        arr = [0]*n
        for i in range(0,length):
            for k in range(bookings[i][0],bookings[i][1]+1):
                arr[k-1]+=bookings[i][2]
        return arr'''
        #ans[i] = ans[i] + ans[i-1]
        #driving a bus, people get out of the bus at i
        #O(n)
        ans = [0] * n
        for start, end, val in bookings:
            ans[start - 1] += val
            if end < n: 
                ans[end] -= val
        for i in range(1, n):
            ans[i] += ans[i - 1]
        return ans
