def fact(num):
    if num==1 or num==2:
        return num
    elif num== len(facts)-1:
        return facts[num]
    else :
        return num*fact(num-1)
        
facts=[1]

j=1
while j<10:
    facts.append(fact(j))
    j+=1
    
# print(facts)

ans=[]
i=1
while True:
    num1=int(str(i)[::-1])
    sum=0
    while num1>0:
        num2=num1%10
        num1//=10
        sum+=facts[int(num2)]
        if(sum==i):
            ans.append(i)
    i+=1
    if len(ans)==4:
        break

print(ans)


# lis = list(str(n).split(""))
# print(facts)