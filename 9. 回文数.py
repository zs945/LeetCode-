import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        out = True
        x = str(x)
        if len(x) == 1:
            out = True
        looptime = int(math.ceil(len(x)/2))
        # 需要判断的次数
        # len(x) 等于 x.__len__()
        start = 0
        end = x.__len__() - 1
        if x.__len__() != 1:
            for i in range(looptime):
                if x[start] == x[end]:
                    start += 1
                    end -= 1
                    out = True
                    continue
                if x[start] != x[end]:
                    out = False
                    break
        return out
if __name__ == '__main__':
     s = Solution()
     x = 121
     c = s.isPalindrome(x)
     print(c)