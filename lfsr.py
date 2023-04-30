import numpy as np

from pylfsr import LFSR

'''
#for 5-bit LFSR with polynomial  x^5 + x^4 +  x^3 + x^2 +1
#state = [0,0,0,1,0]
state = [0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,1,0,1,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,1,1,1,1,]
#state = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
#state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,]
#fpoly = [5,4,3,2]
fpoly = [42, 35, 33, 31, 27, 26, 25, 22, 21, 19, 18, 17, 16, 10, 7, 6, 5, 3, 2, 1]
#        [42, 35, 33, 31, 27, 26, 25, 22, 21, 19, 18, 17, 16, 10, 7, 6, 5, 3, 2, 1,]
#L = LFSR(fpoly=fpoly,initstate =seed)
L = LFSR(initstate=state,fpoly=fpoly,counter_start_zero=False)
print('count \t state \t\toutbit \t seq')
print('-'*50)
for _ in range(111):
    #print(L.count,L.state,'',L.outbit,L.seq,sep='\t')!
    print(L.count,L.state,'',sep='\t')
    L.next()
print('----------Fibonacci')
print('-'*50)
print('Output: ',L.seq)
'''

print('----------  Galois ----------------') # !!!!!!!!!!!!
state = [0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,1,0,1,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,1,1,1,1,] # 0x20A8E6F04EF
state = [0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,1,1,0,0,1,1,0,1,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,1,1,1,1,] # 0xA8E6F04EF
#state = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
#state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,]

#----------------------------------------------------------------------------------
# From: http://www.cdg.org/technology/cdma_technology/a_ross/LongCode.asp          
fpoly =  [42, 35, 33, 31, 27, 26, 25, 22, 21, 19, 18, 17, 16, 10, 7, 6, 5, 3, 2, 1,]
# revert bytes 
# revert: similar output ressult !!!
rfpoly = [1, 2, 3, 5, 6, 7, 10, 16, 17, 18, 19, 21, 22, 25, 26, 27, 31, 33, 35, 42,]


# from TZ
# Polinomial[42] = {1 1 1 1 0 1 1 1 0 0 1 0 0 0 0 0 1 1 1 1 0 1 1 0 0 1 1 1 0 0 0 1 0 1 0 1 0 0 0 0 0 1};
rfpoly = [1, 2, 3, 4, 6, 7, 8, 11, 17, 18, 19, 20, 22, 23, 26, 27, 28, 32, 34, 36, 42]
#----------------------------------------------------------------------------------

# Worked in C++
frpoly = [1, 2, 3, 4, 6, 7, 8, 11, 17, 18, 19, 20, 22, 23, 26, 27, 28, 32, 34, 36,]
#--------------------------------------------------------------------------------------------------------

L = LFSR(initstate=state,fpoly=rfpoly,counter_start_zero=True, conf='galois')
print('count \t state \t\toutbit \t seq')
print('-'*50)
for _ in range(11):
    #print(L.count,L.state,'',L.outbit,L.seq,sep='\t')
    #print(L.count,L.state,'',sep='\t')
    sstate = ''.join(str(s) for s in L.state)
    print('{})\t{}\t{}\t{}'.format(L.count, L.outbit, sstate, hex(int(sstate, 2))))
    L.next()



print('-'*50)
print('Output: ',L.seq)



