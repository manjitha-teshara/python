class Node:

    def __init__(self,d,n=None):
        self.data=d
        self.next=n

class LinkedList:

    def __init__(self,r=None):
        self.root=r
        self.size=0

    def Add(self,item):
        new_node=Node(item,self.root)
        self.root=new_node
        self.size+=1
        return print("added",item)

    def Size(self):
        print(self.size)

    def search(self,item):

        nd=self.root

        while nd:

            if nd.data==item:
                print("Find")

            else:
                nd=nd.next

        return print("no Find")

    def delete(self,item):
        nd=self.root
        prev=self.root

        if nd==self.root:
            nd.next=self.root
            return print("Deleted",item)

        else:
            while prev:
                if nd.data==item:

                    return print("Deleted",item)



                else:
                    nd=self.next
            return print("not find")
                    
li=LinkedList()
print(li.Size())
li.Add(21)
li.Add("Manji")
li.Add(23)
li.Add("teran")
li.Add(5)
li.Add(6)
li.Add(1)
li.delete(23)
li.delete(22222222)
li.delete(5)
li.search("Manji")
li.search(21)
