import sys, os
import time
#import darknet as dn
import cap

#-------------------------
# do_snapshot
#-------------------------
def do_snapshot():
    fname = 'img/' + str(time.time()) + '.jpg'
    ret,x,y = cap.cap(fname,640,480)
    if ret == 0:
        return 0,fname
    else:
        return -1,''
    
            
#-------------------------
# main
#-------------------------
if __name__ == "__main__":    
    print do_snapshot()
