if __name__ == '__main__':
    a=[]
    b=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append(name)
        b.append(score)
    l=(sorted(list(set(b)))[1])
    k=len(b)
    c=[]
    for i in range(k):
        if(b[i]==l):
            c.append(a[i])
    c=sorted(list(set(c)))
    k=len(c)
    for i in range(k):
         print(c[i])
