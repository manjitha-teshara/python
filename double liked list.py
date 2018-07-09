class Node:

    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoubleLikedList:

    def __init__(self,root=None):
        self.root=root
        self.size=0

    def add(self,item):
        newNode=Node(item)
        if self.root:
            newNode.next=self.root
            self.root.prev=newNode
            self.root=newNode
            self.size+=1
            print(item," added 1")
        else:
            self.root=newNode
            self.size+=1
            print(item," added 2")

    def search(self,item):
        temp=self.root
        while temp:
            if temp.data==item:
                return print(item," find")
            else:
                temp=temp.next

        print(item," not find")

    def delete(self,item):
        curNode=self.root
        nextNode=self.root.next

        if curNode.data==item:
            curNode.next=self.root
            curNode.next.prev=None
            self.size-=1
        else:
            while nextNode:
                if nextNode.data==item:
                    curNode.next=nextNode.next
                    nextNode.prev=curNode
                    self.size-=1
                    return print(item," delete 1")
                else:
                    nextNode=nextNode.next
                    curNode=curNode.next
        return print(item," not in list")

        
d=DoubleLikedList()
d.add(23)
d.add(123)
d.delete(23)
d.add("manji")
d.add(12)
d.add("tera")
d.add(45)
d.delete("ha")

