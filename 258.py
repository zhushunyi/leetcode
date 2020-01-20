class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        sum = 0
        while not num == 0:
            digit = num % 10
            num = num // 10
            sum = sum + digit
            #print(sum,num)
            if num == 0 and sum > 9:
                num = sum
                sum = 0
            if num == 0 and sum < 10:
                break
        return sum