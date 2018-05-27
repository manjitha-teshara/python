class Queue():
    def __init__(self):
        self.item=list()

    def isEmpty(self):
        return len(self.item)==0

    def enqueue(self,item):
        self.item.append(item)

    def dequeue(self):
        assert not self.isEmpty()
        return self.items.pop()

    def size(self):
        return len(self.item)


q=Queue()
q.enqueue("dfs")
print(q.isEmpty())
q.enqueue(876)
print(q.size())
q.enqueue("manjitha")
q.enqueue("teshara")
q.enqueue("miya")
q.enqueue("mika")
print(q.size())

