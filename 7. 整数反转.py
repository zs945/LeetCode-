class Solution(object):
    def reverse(self,x):
        """
        :type x: int
        :rtype: int
        """
        listout = []
        out = 0
        start = False
        if x >= 0:
            while (x > 10):
                a = x % 10
                if a == 0:
                    x = x // 10
                else:
                    listout.append(a)
                    start = True
                    x = x // 10
                    break
            while (x > 10 and start == True):
                a = x % 10
                listout.append(a)
                x = x // 10
            if (x == 10):
                listout.append(0)
                listout.append(1)
            if (x < 10):
                listout.append(x)
            listout.reverse()
            for i in range(len(listout)):
                out += listout[i] * (10 ** i)
        if x < 0:
            x = x * -1
            while (x > 10):
                a = x % 10
                if a == 0:
                    x = x // 10
                else:
                    listout.append(a)
                    start = True
                    x = x // 10
                    break
            while (x > 10 and start == True):
                a = x % 10
                listout.append(a)
                x = x // 10
            if (x == 10):
                listout.append(0)
                listout.append(1)
            if (x < 10):
                listout.append(x)
            listout.reverse()
            for i in range(len(listout)):
                out += listout[i] * (10 ** i)
            out = out * -1
        if(out >2**31 - 1 or out < -(2**31)):
            out = 0
        return out
if __name__ == '__main__':
    x = 1534236469
    S = Solution()
    out = S.reverse(x)
    print(out)