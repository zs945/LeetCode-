class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list( s )
        s_ = s.copy()
        lis = []
        out = []
        # hashmap2 = {}
        for i in range(1,len(s_)-1):
            l = i
            r = i
            while(l > 0 and r < len(s_) and s_[l-1] ==s_[r+1]):
                l -= 1
                r += 1
            # hashmap1[i] = s_[l:r+1]
            lis.append(s_[l:r+1])

        for i in range(0,len(s_) - 1):
            l = i
            r = i + 1
            while(l > 0 and r < len(s_) and s_[l] ==s_[r]):
                l -= 1
                r += 1
            # hashmap2[i] = s_[l+1:r]
            lis.append( s_[l+1:r] )

        maxnum = len( lis[0] )
        for i in range(len(lis)-1):
            if len(lis[i+1]) > maxnum:
                maxnum = len(lis[i+1])
        max = maxnum

        for i in range(len(lis)):
            if len(lis[i]) == max:
                out.append(lis[i])
        return out


if __name__ == '__main__':
    c = Solution()
    s = "babad"
    a = c.longestPalindrome(s)
    s1 = "cbbd"
    a1 = c.longestPalindrome( s1 )
    print(a)
    print(a1)
    print("".join(a[0]))
    print( "".join( a1[0] ) )

