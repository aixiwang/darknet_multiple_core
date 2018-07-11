import time,cap
fname = 'data/' + str(time.time()) + '.jpg'
ret,x,y = cap.cap(fname,640,480)
if ret == 0:
    print fname
else:
    pass

        
