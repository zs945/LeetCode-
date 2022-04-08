class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list( s )
        lis = []
        out = []
        # hashmap2 = {}
        # if (len(s) == 1):
        #     lis.append(s[0])
        #     out.append(lis)
        #     out = "".join(out[0])
        # if (len(s) == 2):
        #     if (s[0] == s[1]):
        #         lis.append(s[0])
        #         lis.append(s[1])
        #         out.append(lis)
        #         out = "".join(out[0])
        #     if (s[0] != s[1]):
        #         lis.append(s[0])
        #         out.append(lis)
        #         out = "".join(out[0])
        if (len(s) >= 1 ):
            lis.append(s[0])
            for i in range(1, len(s)-1):
                l = i
                r = i
                while (l > 0 and r < len(s) and s[l-1] == s[r+1]):
                    l -= 1
                    r += 1
                    if (len(s[l:r + 1]) >len(lis[0])):
                    # lis.append(s[l:r + 1])
                        lis[0] = s[l:r + 1]
                    if (l == 0 or r == len(s)-1):
                        break
                # hashmap1[i] = s_[l:r+1]

            for i in range(0, len(s) - 1):
                l = i
                r = i + 1
                while (l >= 0 and r <= len(s)-1 and s[l] == s[r]):
                    if (len(s[l:r + 1]) > len(lis[0])):
                        # lis.append(s[l:r + 1])
                        lis[0] = s[l:r + 1]
                    if (l == 0 or r == len(s)-1):
                        break
                    if (l != 0 and r != len(s)-1):
                        l -= 1
                        r += 1
                # hashmap2[i] = s_[l+1:r]
                # lis.append(s[l + 1:r])

            # maxnum = len(lis[0])
            # for i in range(len(lis) - 1):
            #     if len(lis[i + 1]) > maxnum:
            #         maxnum = len(lis[i + 1])
            # max = maxnum
            #
            # for i in range(len(lis)):
            #     if len(lis[i]) == max:
            #         out.append(lis[i])
            out = "".join(lis[0])
        return out


if __name__ == '__main__':
    c = Solution()
    s ="ccc"
    a = c.longestPalindrome(s)
    print(a)




