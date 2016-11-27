class Node:    #定义节点类
    next=None
    prev=None
    data=None
    def __init__(self,data=0,prev=None,next=None):
        self.next=next
        self.prev=prev
        self.data=data


class DBLink:     #定义链表存储类，有头结点和尾节点
    tail=None
    head=None
    def __init__(self):    #初始化中将头尾节点相连
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head

    def append(self,data):     #在尾节点和前面的节点中插入节点用于创建链表
        p=Node(data)
        p.next=self.tail
        p.prev=self.tail.prev
        self.tail.prev.next=p
        self.tail.prev=p

    def insert_Node(self,data):     #在指定的位置插入节点
        n=int(input("请输入你想要插入位置的数据："))
        p=self.head.next
        q=Node(data)    #要插入的节点
        while p!=self.tail:
            if p.data==n:
                q.next=p.next     #执行插入操作
                q.prev=p
                p.next.prev=q
                p.next=q
            p=p.next    #后移

    def delete_Node(self):
        n=int(input("请输入想要删除节点的数据："))
        p=self.head.next
        q=self.head
        while p!=self.tail:
            if p.data==n:
                htemp=p     #将要删除的节点存储起来，以便最后删除
                p.prev=q     #将删除的节点断开
                q.next=p.next
            p=p.next
            q=q.next
        del htemp   #删除节点

    #原理：分别从前向后和从后向前移动，交换对应的数据
    def reversed_Node(self):    #将链表逆置
        begin=self.head.next
        end=self.tail.prev
        while begin!=end and begin.prev!=end:     #条件，分为有奇数个和偶数个节点，注意头尾节点不用交换
            begin.data,end.data=end.data,begin.data    #前后交换数据
            begin= begin.next    #移动前后节点
            end=end.prev

    def display(self):     #打印所有的节点数据
        p=self.head.next
        while p!=self.tail:
            print(p.data,end=" ")
            p=p.next















if __name__=="__main__":
    app=DBLink()
    x=[33,66,11,99]
    for i in x:
        app.append(i)
    #app.insert_Node(99)
    #app.delete_Node()
    app.reversed_Node()

    app.display()



