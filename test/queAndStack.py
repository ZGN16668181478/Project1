import collections
# 队列先进先出，栈先进后出
queue = collections.deque()
queue.append('shit')
queue.append('oh')
queue.append('fucker')
print(queue)
queue.pop()
print(queue)

