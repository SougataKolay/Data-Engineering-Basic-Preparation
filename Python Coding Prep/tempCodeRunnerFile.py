me="ssougatas"
temp=0
seen=set()
dup=[]
for n in name:
    if n in seen:
        dup.append(n)
    else:
        seen.add(n)
        temp +=1
print(temp)