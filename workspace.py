from Circuit import *
from math import *

z1= 20;z2=15-10j;z3=5+7j;z4=-20
zzhi = ees(z2).chuan(ees(z3).bing(z4))
Izhi = z1/(z1+zzhi.complex)*(ModAngToComplex(1,30))
uab1 = z2*Izhi
print(ees(uab1))
i2 = ModAngToComplex(50,-60)/(ees(z2).chuan(ees(z3).bing(z4)).chuan(z1).complex)
uab2=ModAngToComplex(50,-60) -z2*i2
print(ees(uab2))
print(ees(uab1+uab2))
sss = ees(z3).bing(z4).chuan(z1)
print(sss)
print( ees(z2).bing( sss )   )