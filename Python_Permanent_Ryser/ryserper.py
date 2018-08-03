import numpy as np
import scipy as sp
import time
import multiprocessing as mp
def ryserpers(a,n):
    start_time = time.time()
    per=0
    for i in range((2**n)-1):
        i=i+1
        cols=bin(i)[2:]
        index=[]
        num_col=0
        for j in range(n-len(cols)):
            cols='0'+cols
        for k in range(n):
            if cols[k]=='1':
                index.append(k)
        num_col=len(index)
        par_sum=1
        row_sum=[]
        temp=0
        for l in range(n):
            temp=0
            for m in index:
                temp=temp+int(a[l][m])
            row_sum.append(temp)
        #row_sum.pop(0)
        for p in row_sum:
            par_sum=par_sum*p
  
        par_sum=((-1)**(num_col))*par_sum
        per=par_sum+per
    print (time.time() - start_time, "seconds")
    print('Permanent: ', per)
    return per
            
        
def ryserperp(a,n,init,qu):
    
    #per=np.int64(0)
    per=0
    for i in range(init,(2**n),8):
        cols=bin(i)[2:]
        index=[]
        num_col=0
        for j in range(n-len(cols)):
            cols='0'+cols
        for k in range(n):
            if cols[k]=='1':
                index.append(k)
        num_col=len(index)
        par_sum=1
        row_sum=[]
        temp=0
        for l in range(n):
            temp=0
            for m in index:
                temp=temp+a[l][m]
            row_sum.append(int(temp))
        #row_sum.pop(0)
        for p in row_sum:
            par_sum=par_sum*p
      
        par_sum=((-1)**(num_col))*par_sum
        #parts[i]=par_sum
        per=par_sum+per
   #commented out in order to have cleaner output!! #print ('process',init, per)
   # parts[init-1]=np.int64(per)
    qu.put(per)
    return per
	    
