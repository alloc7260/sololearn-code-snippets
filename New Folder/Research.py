import numpy_financial as npf

res = npf.pv(rate = 0.10, nper=8, pmt=0, fv=1000)
print(res)
res = npf.fv(rate=0.08, nper=5, pmt=0, pv=-1000)
print(res)
res = npf.pmt(rate=0.07/12, nper=5*12, pv=100000, fv=0) 
print(res)
res = npf.pmt(rate=0.10/12, nper=5*12, pv=0, fv=50000) 
print(res)