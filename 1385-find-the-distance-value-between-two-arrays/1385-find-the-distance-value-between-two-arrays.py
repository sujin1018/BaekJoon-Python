class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        result = 0
        for i in arr1:
                if all(abs(i-j) > d for j in arr2):
                    result +=1
        return result