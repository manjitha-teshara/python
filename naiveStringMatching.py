def naiveStringMatching(p,t):#pattern cheak left to rigth
    plen=len(p)
    tlen=len(t)
    for i in range(0,tlen-plen+1):
        count=0
        for j in range(0,plen):
            if p[j]==t[i+j]:
                count+=1
        if count==plen:
            return print("String matching in ",i," index")
p="Colombo"
t="University of Colombo and the Institute of Computer Technology and considered as the leading computing"
naiveStringMatching(p,t)
