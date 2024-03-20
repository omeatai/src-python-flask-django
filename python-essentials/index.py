from decimal import Decimal, getcontext

getcontext().prec = 2
u = Decimal(1) / Decimal(3)
print(u)
