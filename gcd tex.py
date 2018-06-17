

def gcd(x,y):

    while x!=y:

        if x>y:
            x=x-y
        else:
            y=y-x
    print("GCD is ",x)



while True:
    x=int(input(''))
    y=int(input(''))
    
    if str(x)=='':
        True
    else:
        gcd(x,y)
        
