import heapq
'''heapq是数据结构中的堆操作，主要的函数：
heappush(heap,items):将items压入堆数组中
heappop(heap):删除堆数组中的最小值
heapreplace(heap,items):先删除堆数组中的最小值
'''


'''
nums=[23,4,5,6,7,-1,445,-4,677,666,90]
print(heapq.nlargest(3,nums))   #打印出最大的3个数
print(heapq.nsmallest(3,nums))  #返回最小的三个数
'''
x=[9,88,66,55]   #此处的x是list,并没有变成堆
heapq.heappop(x)  #这里返回的并不是最小值，因为x并不是堆
print(x)
heapq.heapify(x)  #将x转化成堆数组
print(heapq.heappop(x))  #此处删除的才是堆数组中最小的
print(x)
heapq.heapreplace(x,99)   #这里是删除最小的，然后将99压入堆底  与heappushpop(x,items)相反
print(x)





'''
for i in range(0,5):
    heapq.heappush(heap,i)   #将内容压入堆数组中


print(heapq.heappushpop(heap,99))   #这个函数的功能是先将99写入堆数组中，然后删除堆中的最小值并返回
print(heapq.heappushpop(heap,-8))   #这里相当于没有添加元素，因为-8添加进去后变成了最小的，然后又被删除了


print(heapq.heappop(heap))  #删除堆数组中最小的并且返回
heap.append(-9)             #这是对数组的普通在末尾添加元素的操作，在这里并没有实际的写入堆中
print(heap)
print(heapq.heappop(heap))  #这里并没有删除-9，因为上面的-9是通过append 添加进去的
heapq.heappush(heap,99)     #在这里才将-9实际的写入堆数组中
print(heapq.heappop(heap))
'''



