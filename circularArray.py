class CircularArray:

    def __init__(self):
        self.maxSize=5#len(self.ist)
        self.list=[]
        self.back=-1
        self.front=-1
        self.count=0

    def enequeue(self,item):
        
        self.back=(self.back+1)%self.maxSize
       # print(self.back)
        if(self.back!=0):
            #self.front=(self.front+1)%self.maxSize
            self.list.insert(self.back,item)
            self.count+=1
        else:
            if self.count==self.maxSize:
                print("Circular queue is full")
            else:
                #self.front=(self.front+1)%self.maxSize
                self.list.insert(self.back,item)
                self.count+=1
    def dequeue(self):
       # print(self.back)
        self.front=(self.front+1)%self.maxSize
        self.list.pop(self.front)
        #self.front=(self.front+1)%self.maxSize
        self.count-=1
                


cc=CircularArray()
cc.enequeue("A")
cc.enequeue("B")
cc.enequeue("C")
print(cc.front)
print(cc.list)
cc.dequeue()

cc.enequeue("D")
cc.enequeue("E")
cc.enequeue("F")
cc.dequeue()


    
    
