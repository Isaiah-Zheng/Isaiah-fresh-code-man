
l1=[2,3,4,5]
l2=[3,2]

a = 0
b = 0
for i in range (len(l1)-1,-1,-1):
    a += l1[i]*(10**i)
for j in range (len(l2)-1,-1,-1):
    b += l2[j]*(10**j)
c = a + b
c = str(c).split()
c = list(c)
c.reverse()
for k in c:
    int(k)

print(c)