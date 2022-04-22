class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 两个指针i,j
        # 当两个指针都指到最后一个元素的时候，结束循环，返回ture，反之返回flase
        # "*"相当于让前一个字符0个或任意个
        cache = [[False] * (len(s)+1) for _ in range(len(p)+1)]
        #创建一个len(p)+1)行 len(s)+1列的全False二维数组
        cache[0][0] = True
        # 第一行第一个与第一列第一个都是空，设置[0][0]为ture
        for i in range(1,len(p)):
            cache[i+1][0] = cache[i-1][0] and p[i] == "*"
        # 因为'*' 匹配零个或多个前面的那一个元素，例如“a*”，“a*b*”，“.*”将可以匹配空

        for i in range(len(p)):
            # 循环第i行
            for j in range(len(s)):
                # 循环第j列
                if p[i] == "*":
                    # p的第i个元素为“*”
                    cache[i+1][j+1] = cache[i][j+1] or cache[i-1][j+1]
                    # 如果p的第i个元素为“*”那么只要p的前i-1个或者前i-2个元素与s的前j个元素匹配，那么p的前i个元素就与s的前j个元素匹配
                    if p[i-1] == s[j] or p[i-1] == ".":
                        # 考虑特殊情况，p[i]的前一个元素是字母与s的第j个元素相同，或者前一个元素是“.”
                        cache[i+1][j+1] |= cache[i+1][j]
                        # 只要p的前i个元素与s的前j-1个元素匹配，那么p的前i个元素与s的前j个元素就匹配
                        # |就是或的意思a|=b 是a = a|b 只要有一个是ture结果就是ture，否则为false
                else:
                    # p的第i个元素不是“*”，当p的前i-1个元素与s的前j-1个元素匹配时，只要p的第i个元素是字母与s的第j个元素相等或者p的第i个元素为“."，那么p的前i个元素与s的前j个元素匹配
                    cache[i+1][j+1] = cache[i][j] and (p[i] == s[j] or p[i] == ".")
        # print(cache)
        return cache[-1][-1]


if __name__ == '__main__':
    s = "aab"
    p = "c*a*b"
    S = Solution()
    out = S.isMatch(s,p)
    print(out)