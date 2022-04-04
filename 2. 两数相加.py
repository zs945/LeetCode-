class Solution(object):

    def calc(self, number):
        result = []
        while number:
            result.append( number % 10 )
            number = number // 10
        # 逆序，按正常的顺序返回
        # result.reverse()
        return result

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = 0
        b = 0
        for i in range(0,len(l1)):
            a += l1[i]*(10**i)
        for j in range(0,len(l2)):
            b += l2[j]*(10**j)
        return a + b
if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    c = Solution()
    d = c.addTwoNumbers(l1,l2)
    print(d)
    print(c.calc(d))
