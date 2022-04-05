class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        s = list(s)
        outs = []
        for i in range(numRows):
            if i == 0:
                a = 0
                while a < len(s):
                    outs.append(s[a])
                    a += 2*numRows - 2

            if i == numRows-1:
                a = numRows-1
                while a < len(s):
                    outs.append(s[a])
                    a += 2*numRows - 2

            if i != numRows-1 and i != 0:
                a = i
                b = 2
                while a < len(s):
                    outs.append(s[a])
                    if b%2 == 0:
                        a += 2*numRows - 2 - 2*i
                        b += 1
                    else:
                        a += 2 * i
                        b += 1
        return "".join(outs)

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    S = Solution()
    out = S.convert(s,numRows)
    print(out)

# PAHNAPLSIIGYIR