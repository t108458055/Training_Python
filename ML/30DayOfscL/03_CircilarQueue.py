"""_summary_ 環形佇列Queue
define : 以一維陣列CQ(0~n-1)表示一個環狀佇列
        意旨指標front 指向佇列前端元素的前一個位置，指標rear則指向佇列尾端的

"""
from collections import deque
## 定義一 8個 元素 環形佇列
########### front - - - - rear
cq = deque([11,22,33,44,55,66], maxlen = 8) ## 如圖
cq.append(77) # 加入 77
cq.extend([88]) # 延伸 88

# [11,22,33,44,55,66,77,88]
print(cq.pop())  # [11,22,33,44,55,66,77] --> 88

# 旋轉指標 Rotate the pointer
cq.rotate(-1)

# at this point you have [22,33,44,55,66,77,11]
print(cq.pop())  # [22,33,44,55,66,77] --> 11
print(cq.pop())  # [22,33,44,55,66] --> 77
print(cq.pop())  # [22,33,44,55] --> 66
print(cq.pop())  # [22,33,44] --> 55