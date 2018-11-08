# 1. first glance solution, not so robust
from decimal import *
getcontext().prec = 3000
digit_list = [0]
for i in range(1001):
    r = str(Decimal(1) / Decimal(i + 1))
    digit_list.append(r.find(r[5:11], 11))
print(digit_list.index(max(digit_list)))


# 2. another better solution
digit_list = [0]
remainder_list = []
for i in range(1, 1001):
    last_r = 1 % i
    while last_r not in remainder_list:
        remainder_list.append(last_r)
        last_r = (last_r * 10) % i
    digit_list.append(len(remainder_list))
    remainder_list.clear()
print(digit_list.index(max(digit_list)))
