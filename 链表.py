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




if __name__ == '__main__':
    ll = SingleLinkList()
    print( ll.is_empty() )
    print( ll.length() )
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.add(8)
    ll.insert(1,9)
    ll.insert(2,9)
    ll.travel()
    ll.remove(9)
    ll.travel()
