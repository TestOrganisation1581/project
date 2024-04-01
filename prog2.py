f=open('17_13088.txt')
a=list(int(x) for x in f)
f.close()
r=[]
for i in range(len(a)):
    if abs(a[i])%100==17:
        r.append(a[i])
q=max(r)
e=[]
for i in range(len(a)-2):
    w=0
    if len(str(a[i]))==4:
        w=w+1
    if len(str(a[i+1]))==4:
        w=w+1
    if len(str(a[i+2]))==4:
        w=w+1
    if (a[i]+a[i+1]+a[i+2]>q) and (w==2) and (abs(a[i])%5==0 or abs(a[i+1])%5==0 or abs(a[i+2])%5==0 ):
        e.append(a[i]+a[i+1]+a[i+2])
    w=0
print(len(e),max(e))