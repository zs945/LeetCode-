class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        s_ = s.copy()
        numlist = []
        hashmap = {}
        i = 1
        a = 1
        if (len(s) == 0):
            numlist.append(0)
        if (len(s)>0):
            for index in range(len(s_) - 1):
                if len(s) == 1:
                    i = 1
                    numlist.append(i)
                    break
                another_num = s[0]
                hashmap[-1] = another_num
                # print(hashmap)
                if s[a] in hashmap.values():
                    # return [hashmap.keys(another_num), index]
                    numlist.append(i)
                    for j in range(a):
                        s.pop(0)
                    hashmap.clear()
                    a = 1
                    i = 1
                else:
                    i += 1
                    a += 1
                    hashmap[index] = s_[index + 1]
        # return max(numlist),numlist
        return max(numlist)
if __name__ == '__main__':

    c = Solution()
    s1 = ""
    s2 = "bbbbb"
    s3 = "pwwkew"
    num1=  c.lengthOfLongestSubstring(s1)
    print(num1)
    # num2 =  c.lengthOfLongestSubstring(s2)
    # num3 =  c.lengthOfLongestSubstring(s3)
    # print(s1,num1,s2,num2,s3,num3)