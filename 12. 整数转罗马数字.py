class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        loma = "MDCLXVI"
        lomanumble = [1000,500,100,50,10,5,1]
        outlist = []
        outstr = []
        for i in range(len(lomanumble)):
            outlist.append(num//lomanumble[i])
            num = num%lomanumble[i]
        for i in range(len(outlist)):
            if i == 2 and outlist[i] == 4 and outlist[i-1] != 1:
                outstr.append("CD")
                continue
            if i == 2 and outlist[i] == 4 and outlist[i-1] == 1:
                outstr.pop()
                outstr.append("CM")
                continue
            if i == 4 and outlist[i] == 4 and outlist[i-1] != 1:
                outstr.append("XL")
                continue
            if i == 4 and outlist[i] == 4 and outlist[i-1] == 1:
                outstr.pop()
                outstr.append("XC")
                continue
            if i == 6 and outlist[i] == 4 and outlist[i - 1] != 1:
                outstr.append("IV")
                continue
            if i == 6 and outlist[i] == 4 and outlist[i - 1] == 1:
                outstr.pop()
                outstr.append("IX")
                continue
            for j in range(outlist[i]):
                outstr.append(loma[i])
        out = "".join(outstr)
        return out



if __name__ == '__main__':
    num = 1994
    S = Solution()
    out = S.intToRoman(num)
    print(out)