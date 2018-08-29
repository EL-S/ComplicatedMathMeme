from random import randint
from math import *

#factors numbers so that the math looks more random and less intuitive
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

loops_1 = 1 #first section with factorising

num = "(x-1)"
a = num
for i in range(loops_1):
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

number = a
orig_number = num

#number = "x^2 - 1"
#orig_number = "(x-1)(x+1)"

symbols = ["+","-","*","/"]
symbols_2 = ["/","*"]
symbols_3 = ["*","/"]
symbols_4 = ["-","+","/","*"]

loops_2 = 2 #loops in second section with forming equation
lower = 0
upper = 1000
total_right = ""
total_left = ""

for i in range(loops_2):
    r = randint(lower,upper)
    index_for_symbol = randint(0,3)
    index_for_symbol_2 = randint(0,1)
    symbol = symbols[index_for_symbol]
    symbol_2 = symbols_2[index_for_symbol_2]
    symbol_3 = symbols_3[index_for_symbol_2]
    symbol_4 = symbols_4[index_for_symbol]
    r_3 = randint(lower,upper)
    r_1 = str(r) + symbol_3 + "(1/"+str(r_3)+")"
    r_2 = str(r) + symbol_2 + str(r_3)
    if i == 0:
        total_right = "((("+str(number)+")"+str(symbol)+str(r)+")"+str(symbol_4)+str(r)+")"
        total_left = "((("+str(orig_number)+")"+str(symbol)+str(r)+")"+str(symbol_4)+str(r)+")"
    else:
        total_right = "((((("+str(total_right)+")"+str(symbol)+"("+str(number)+"))"+str(symbol_4)+"("+str(orig_number)+"))"+str(symbol)+"(("+str(r_1)+")"+symbol_2+"2))"+str(symbol_4)+"(("+str(r_2)+")"+symbol_2+"2))"
        total_left = "((((("+str(total_left)+")"+str(symbol)+"("+str(orig_number)+"))"+str(symbol_4)+"("+str(number)+"))"+str(symbol)+"(("+str(r_1)+")"+symbol_3+"(1/2)))"+str(symbol_4)+"(("+str(r_2)+")"+symbol_3+"(1/2)))"
print(total_left,"=",orig_number)



