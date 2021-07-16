# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Time    : 2021/5/31 17:07
# @File    : Q495_findPoisonedDuration.sql
# @Note    :

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0:
            return 0
        res = 0
        left = timeSeries[0]
        for i in range(1,len(timeSeries)):
            left += duration
            if left <= timeSeries[i]:
                res += duration
                left = timeSeries[i]
            elif left > timeSeries[i]:
                res = res + timeSeries[i] - timeSeries[i - 1]
                left = timeSeries[i]

        return res + duration
