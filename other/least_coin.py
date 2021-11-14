lis= [1,2,5,10,20,50,100,200,500,2000]
n=int(input("Enter amount: "))
coins=[]
length = len(lis)
while length-1>=0:
    if (lis[length-1]<=n):
        n-=lis[length-1]
        coins.append(lis[length-1])
    else :
        length-=1
    
print(coins)