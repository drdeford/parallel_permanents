import multiprocessing as mp
import numpy as np
from ryserper import *
if __name__ == '__main__':
    
    jobs=[]
    #permanent=0
    permanent2=0
    #empty=[]
    pers=[]
    #qset=[[],[],[],[],[],[],[],[]]
    #for i in range(8):
        #qset[i]=mp.Queue()
    q2=mp.Queue()
    n=input('Size of Matrix: ')
    n=int(n)
    a=np.random.random_integers(0,1,size=(n,n))
    #ryserpers(a,n)
    start_time = time.time()
   # for i in range(8):
    #    empty.append(0)
    #parts=mp.Array('l',np.array(empty,dtype='int64'))
    for init in range(1,9):
        p=mp.Process(target=ryserperp,args=(a,n,init,q2,))
        jobs.append(p)
        p.start()
        
        #p.join()
    for m in range(8):
        jobs[m].join()
    for m in range(8):
        pers.append(q2.get())
    #p.join()
    #for k in parts:
     #   permanent=permanent+k
    for k in pers:
        permanent2=permanent2+k
    #print(parts[:])
   # print('Parts ',permanent)
   # print(q2)
    print('Permanent: ', permanent2)
    #print(pers[:])
    print (time.time() - start_time, "seconds")
