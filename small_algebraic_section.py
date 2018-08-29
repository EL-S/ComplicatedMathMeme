from random import randint
from math import *

number = "pi"
orig_number = "2pi/2"

#number = "x^2 - 1"
#orig_number = "(x-1)(x+1)"

symbols = ["+","-","*","/"]
symbols_2 = ["/","*"]
symbols_3 = ["*","/"]
symbols_4 = ["-","+","/","*"]

loops = 4 #loops
lower = 0
upper = 1000
total_right = ""
total_left = ""

for i in range(loops):
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
