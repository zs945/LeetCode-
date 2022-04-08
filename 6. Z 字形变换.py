class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        outs = []
        s = list(s)
        if(len(s) == 1 or numRows == 1):
            for i in range(len(s)):
                outs.append(s[i])
        if(len(s) != 1 and numRows != 1):
            for i in range(numRows):
                if i == 0 or i == numRows - 1:
                    a = i
                    while a < len(s):
                        outs.append(s[a])
                        a += 2 * numRows - 2

                # if i == numRows-1:
                #     a = numRows-1
                #     while a < len(s):
                #         outs.append(s[a])
                #         a += 2*numRows - 2

                if i != numRows - 1 and i != 0:
                    a = i
                    b = 2
                    while a < len(s):
                        outs.append(s[a])
                        if b % 2 == 0:
                            a += 2 * numRows - 2 - 2 * i
                            b += 1
                        else:
                            a += 2 * i
                            b += 1
        return "".join(outs)

if __name__ == '__main__':
    s = "AB"
    numRows = 1
    S = Solution()
    out = S.convert(s,numRows)
    print(out)

# PAHNAPLSIIGYIR