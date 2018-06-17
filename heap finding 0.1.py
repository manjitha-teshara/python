a=[1,34,2,45,3,67,4,34,34,34,32,6]



def heap(a):
    collecter=[]
    for i in range(0,len(a)-1):
        
        i1=i+1
        i2=i+2

        if (a[i1]>= a[i]) and (a[i2]<=a[i1]):

           
            collecter.append(a[i1])

            
    collecter.sort()
    #print(collecter)
    print(collecter[len(collecter)-1])
    

heap(a)
