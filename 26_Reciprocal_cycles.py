from decimal import *
getcontext().prec = 3000
itv = 10

for i in range(1000):
    r = str(Decimal(1) / Decimal(i + 1))

    if r.find(r[5:11],11) > 986:
        print(i+1, r, r.find(r[5:11],11))
