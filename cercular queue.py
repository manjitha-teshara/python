class CircularQueue:

    def __init__(self):
        self.qlist=[]
        self.max=8 #8 node circular queue
        self.front=-1
        self.back=-1
        self.count=0

    def enequeue(self,item):

        if self.count !=self.max:
            self.back=(self.back+1)%self.max
            self.qlist.insert(self.back,item)
            self.count+=1
            return print(item," added")
        else:
            print("Queue is full")
    def dequeue(self):

        if self.count!=0:
            self.front=(self.front+1)%self.max
            self.qlist.pop(self.front)
            self.count-=1
            return print("deleted")
            
        
cq=CircularQueue()
cq.enequeue(23)
cq.enequeue(45)
cq.dequeue()
cq.enequeue(231)
cq.enequeue(425)
print(cq.qlist)
cq.enequeue(231)
cq.enequeue(451)
cq.dequeue()
cq.enequeue(2311)
cq.enequeue(4251)
print(cq.qlist)
cq.enequeue("ma")
cq.enequeue("as")
cq.dequeue()
cq.enequeue("sad")
cq.enequeue("asd")
print(cq.qlist)

