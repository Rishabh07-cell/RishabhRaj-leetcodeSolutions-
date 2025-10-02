class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        timeSeries.sort()
        res, upper = 0, 0
        for i, num in enumerate(timeSeries): 
            if num > upper: upper = num
            res, upper = res + num + duration - upper, num + duration
        return res
