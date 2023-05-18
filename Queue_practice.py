import queue as q

q1 = q.Queue()
q1.put(1)
q1.put(2)
q1.put(3)
q1.put(4)
print(q1.get())
print(q1.get())

q2 = q.LifoQueue()
q2.put(1)
q2.put(2)
q2.put(3)
q2.put(4)
print(q2.get())
print(q2.get())


q3 = q.PriorityQueue()
q3.put((4,'RED'))
q3.put((5,'yellow'))
q3.put((7,'blue'))
q3.put((1,'green'))
print(q3.get())
print(q3.get())