class Solution(object):
    def myAtoi(self,s):
        """
        :type s: str
        :rtype: int
        """
        outlist = []
        Symbolic = 1
        switch = 1
        out = 0
        s = list(s)
        if len(s) == 1 and s[0].isdigit() == False:
            out = 0
        if len(s) == 1 and s[0].isdigit() != False:
            out = int(s[0])
        if len(s) > 1:
            for i in range(len(s)):
                if switch == 1 and s[i] == " ":
                    continue
                if s[i] == "-":
                    if s[i + 1].isdigit() == False:
                        out = 0
                        break
                    Symbolic = Symbolic * -1
                    switch = 0
                    continue
                if s[i] == "+":
                    if s[i + 1].isdigit() == False:
                        out = 0
                        break
                    Symbolic = Symbolic * 1
                    switch = 0
                    continue
                if s[i].isdigit() == True:
                    switch = 0
                    outlist.append(int(s[i]))
                    if i == len(s) - 1:
                        break
                    if i != len(s) - 1:
                        if s[i+1].isdigit() == False:
                            break
                    continue
                if s[i].isdigit() == False:
                    break

        outlist.reverse()
        for i in range(len(outlist)):
            out += outlist[i] * (10 ** i)
        out =  out * Symbolic
        if out > 2**31 - 1:
            out = 2**31 - 1
        if out < -1 * 2**31:
            out = -1 * 2**31
        return out


if __name__ == '__main__':
    S = Solution()
    s = "00000-42a1234"
    out = S.myAtoi(s)
    print(out)