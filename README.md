# -Datastructure-Queue
Practice and learn Data structure Queue with python

## 簡介：

類似於堆疊的結構但是與堆疊不同的地方在於，佇列分成前後端有一個出口跟一個入口。

#佇列以及堆疊都是抽象資料型態(Abstract data type,ADT)，都可以透過串列或是陣列來實作

## 特性:

- 有兩個端點，前端與後端
- 後端只能新增資料
- 前端只能刪除或是讀取資料
- 資料存取必須符合先進先出(FIFO)

## 構造:

根據不同的使用方式python提供了三種不同的queue實作

1. Queue(FIFO): 先進先出的queue
2. LifoQueue(LIFO): 後進先出的queue
3. PriorityQueue: 根據優先順序來決定輸出的queue，因此在輸入時就必須多帶一個key來指定優先順序

## 儲存方式:

以python 為例可以使用queue這個套件

也可以使用陣列或是串列去實作佇列

```python
import queue as q

q1 = q.Queue() #Queue(-1) 不限定佇列長度，若帶入4則代表佇列長度最大為4
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
```

如果佇列達到最大容量則該執行會暫停直到佇列有更多的空間才會繼續執行

## 常用範例:

環狀佇列: 例如行車紀錄器，會自動記錄5天的資料，如果有第六天的資料要加入這個記憶體中就像佇列的行為一樣，如果我們將橫向的表示法變成一個圓形就可以將D1的資料替換為D6的資料並且將前端的指標指向D2後端的指標指向D6，就完成一個環狀佇列。

| D1 | D2 | D3 | D4 | D5 | D6 |
| --- | --- | --- | --- | --- | --- |
| 前端 |  |  |  | 尾端 |  |
| 輸出(get()) | 前端 |  |  |  | 尾端put() |

優先佇列: 往往使用在我們想在某個list當中按照有先順序取值的時候，因此就必須在將數值放入佇列之前附加優先權眾給每一個數值，q.put((1,’Red’)) 或是 q.put((’a’,1))，如此一來queue就會根據key的排序來將結果pop出來
