class Node( object ):
    def __init__(self, elem):
        self.elem = elem
        self.next = None
class SingleLinkList( object ):
    def __init__(self, node=None):
        self._head = None
    def is_empty(self):
        return self._head == None
        # 判断链表是否为空
    def length(self):
        # cur游标用来移动遍历节点
        cur = self._head
        # count 用来记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
        # 判断链表长度
    def travel(self):
        cur = self._head
        while cur != None:
            print( cur.elem,end= " ")
            cur = cur.next
        # 遍历整个链表
    def add(self, item):
        # 链表头部添加元素
        node = Node(item)
        node.next = self._head
        self._head = node
    def append(self, item):
        node = Node( item )
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
        # 链表尾部添加元素
    def insert(self, pos, item):
        # pos：链表的下标
        # 指定位置插入元素
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            node = Node( item )
            pre = self._head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node
    def remove(self, item):
        # 删除节点
        cur = self._head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断此结点是不是头结点
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
    def search(self, item):
        # 查找节点是否存在
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ll1 = SingleLinkList()
        ll2 = SingleLinkList()

        def ConstructSingleLinkList(ll, a):
            for i in range( 0, len( a ) ):
                ll.append( a[i] )
            return ll

        lll1 = ConstructSingleLinkList( ll1, l1 )
        lll2 = ConstructSingleLinkList( ll2, l2 )
        lll3 = SingleLinkList()
        cur1 = lll1._head
        cur2 = lll2._head
        # print( cur1.type )
        # print(cur1.next != None)
        # count = 0
        # while(cur1.next != None and cur1.next != None)
        for j in range( 0, max( lll1.length(), lll2.length() ) ):
            # print( cur1.next != None )
            # print(cur1.type)
            # print(4)
            if cur1.next != None and cur2.next != None:
                # print(1)
                a = cur1.elem + cur2.elem
                if a > 9:
                    lll3.append( a % 10 )
                    # print( "第二个0" )
                    cur1.next.elem = cur1.next.elem + 1
                    cur2 = cur2.next
                    cur1 = cur1.next
                else:
                    lll3.append( a )
                    # print("第一个7")
                    cur1 = cur1.next
                    cur2 = cur2.next
            if cur1.next == None and cur2.next != None:
                # print(2)
                a = cur1.elem + cur2.elem
                if a > 9:
                    lll3.append( a % 10 )
                    # cur1 = cur1.next
                    cur2.next.elem = cur2.next.elem + 1
                    for i in (0, lll2.length() - (lll1.length())):
                        if cur2.next != None:
                            cur2 = cur2.next
                            lll3.append( cur2.elem )
                    break
                else:
                    lll3.append( a )
                    for i in (0, lll2.length() - (lll1.length())):
                        if cur2.next != None:
                            cur2 = cur2.next
                            lll3.append( cur2.elem )
                    break
            if cur1.next != None and cur2.next == None:
                # print(3)
                a = cur1.elem + cur2.elem
                # cur2 = cur2.next + 1
                if a > 9:
                    # cur2 = cur2.next + 1
                    lll3.append( a % 10 )
                    cur1.next.elem = cur1.next.elem + 1

                    for i in (0, lll1.length() - (lll2.length())):
                        if cur1.next != None:
                            cur1 = cur1.next
                            lll3.append( cur1.elem )
                    break

                else:
                    lll3.append( a )
                    for i in (0, lll1.length() - (lll2.length())):
                        if cur1.next != None:
                            cur1 = cur1.next
                            lll3.append( cur1.elem )
                    break
            if cur1.next == None and cur2.next == None:
                # print(3)
                a = cur1.elem + cur2.elem
                # cur2 = cur2.next + 1
                if a > 9:
                    # cur2 = cur2.next + 1
                    lll3.append( a % 10 )
                    lll3.append( a // 10 )
                    break
                else:
                    lll3.append( a )
                    # print( "第三个8" )
                    break
        # lll3.travel()
        return lll3
if __name__ == '__main_' \
               '_':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    a = Solution()
    l3 = a.addTwoNumbers(l1,l2)
    # l3.travel()
    # ll1 = SingleLinkList()
    # ll2 = SingleLinkList()
    # def ConstructSingleLinkList(ll,a):
    #     for i  in range(0,len(a)):
    #         ll.append(a[i])
    #     return ll
    # lll1 = ConstructSingleLinkList(ll1,l1)
    # lll2 = ConstructSingleLinkList(ll2,l2)
    # lll3 = SingleLinkList()
    # cur1 = lll1._head
    # cur2 = lll2._head
    # # print( cur1.type )
    # # print(cur1.next != None)
    # # count = 0
    # # while(cur1.next != None and cur1.next != None)
    # for j in range(0,max(lll1.length(),lll2.length())):
    #     # print( cur1.next != None )
    #     # print(cur1.type)
    #     # print(4)
    #     if cur1.next != None and cur2.next != None:
    #         # print(1)
    #         a = cur1.elem + cur2.elem
    #         if a > 9:
    #             lll3.append(a%10)
    #             # print( "第二个0" )
    #             cur1.next.elem = cur1.next.elem + 1
    #             cur2 = cur2.next
    #             cur1 = cur1.next
    #         else:
    #             lll3.append(a)
    #             # print("第一个7")
    #             cur1 = cur1.next
    #             cur2 = cur2.next
    #     if  cur1.next == None and cur2.next != None:
    #         # print(2)
    #         a = cur1.elem + cur2.elem
    #         if a > 9:
    #             lll3.append(a%10)
    #             # cur1 = cur1.next
    #             cur2.next.elem = cur2.next.elem + 1
    #             for i in (0,lll2.length()-(lll1.length())):
    #                 if cur2.next != None:
    #                     cur2 = cur2.next
    #                     lll3.append( cur2.elem )
    #             break
    #         else:
    #             lll3.append(a)
    #             for i in (0, lll2.length() - (lll1.length())):
    #                 if cur2.next != None:
    #                     cur2 = cur2.next
    #                     lll3.append( cur2.elem )
    #             break
    #     if  cur1.next != None and cur2.next == None:
    #         # print(3)
    #         a = cur1.elem + cur2.elem
    #         # cur2 = cur2.next + 1
    #         if a > 9:
    #             # cur2 = cur2.next + 1
    #             lll3.append( a % 10 )
    #             cur1.next.elem = cur1.next.elem  + 1
    #
    #             for i in (0, lll1.length() - (lll2.length())):
    #                 if cur1.next != None:
    #                     cur1 = cur1.next
    #                     lll3.append( cur1.elem )
    #             break
    #
    #         else:
    #             lll3.append( a )
    #             for i in (0, lll1.length() - (lll2.length())):
    #                 if cur1.next != None:
    #                     cur1 = cur1.next
    #                     lll3.append( cur1.elem )
    #             break
    #     if  cur1.next == None and cur2.next == None:
    #         # print(3)
    #         a = cur1.elem + cur2.elem
    #         # cur2 = cur2.next + 1
    #         if a > 9:
    #             # cur2 = cur2.next + 1
    #             lll3.append( a % 10 )
    #             lll3.append(a//10)
    #             break
    #         else:
    #             lll3.append( a )
    #             # print( "第三个8" )
    #             break
    # lll3.travel()








