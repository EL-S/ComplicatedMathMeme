from random import randint
from math import *

def factor(r):
    t = r
    z = t**(1/2)
    p = z%1
    f = []
    e = 3
    s = 2
    q = int(t/2) + 1
    if t%2 == 0:
        e = 2
        s = 1
    if p != 0:
        y = floor(z)
    else:
        y = int(z) + 1
    for j in range(e,y,s):
        d = (t/j);
        if (t%j) != 0:
            continue
        for k in range(e,q,s):
            if j*k == t:
                h = [j,k]
                f.append(h)
                break
    if not f:
        f.append([1,t])

    else:
        f.append([1,t])
    return f

a = "2";
for i in range(2):
    y = randint(0,2)
    if y != 0:
        r = randint(1,1000)
        l = factor(r)
        o = randint(1,len(l)) - 1
        if len(l) >= 2:
            g = l[o]
            b = g[0]
            w = g[1]
            o = randint(1,len(l)) - 1
            u = l[o]
            if u == g:
                while u == g:
                    o = randint(1,len(l)) - 1
                    u = l[o]
            
            a = "("+"("+str(u[0]/4)+"+"+str((u[0]/4)*3)+")"+"*"+str(u[1])+")"+"("+a+")"+"/"+"("+str(b)+"*"+str(w)+")"
            x = "("+a+")";
            a = x + "^2" + "/" + x;
        else:
            g = l[o]
            b = g[0]
            w = g[1]
            a = str(r)+"("+a+")"+"/"+str(r)
    else:
        x = "("+a+")";
        a = x + "^2" + "/" + x;
print(a)



