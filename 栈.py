'''下面是用pythnon写的数据结构中的栈的实现，当然想要实现栈可以有更简便的方法，列表本身就可以当成站来使用，这里只是用来练手的一个项目'''
class stack:
    maxsize=None     #想要存储的最大数量
    top=None          #当前的元素的索引
    listArray=None    #列表实现栈
    def __init__(self,size):
        self.maxsize=size
        self.top=0
        self.listArray=[]

        #将元素压入栈中
    def push(self,data):
        if self.top>=self.maxsize:
            print("栈是满的")
        else:
            self.listArray.append(data)
            self.top+=1

      #删除栈的最上面的元素
    def pop(self):
        if self.top<1:
            print("栈是空的")
        else:
            p=self.listArray[self.top-1]
            self.top-=1
            return p

       #打印栈内的元素
    def display(self):
        if self.top==0:
            print("栈是空的")
        else:
            for i in self.listArray[:self.top]:    #利用列表的切片实现栈的输出
                print(i,end=" ")



if __name__=="__main__":
    app=stack(9)
    app.push(99)
    app.push(88)
    app.pop()
    app.display()
