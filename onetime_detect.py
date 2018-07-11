import sys, os
import time
import darknet as dn
import cap
#-------------------------
# main
#-------------------------
if __name__ == "__main__":    
    dn.set_gpu(0)
    fname = 'data/' + str(time.time()) + '.jpg'
    ret,x,y = cap.cap(fname,640,480)
    if ret == 0:
        net = dn.load_net("cfg/yolov3-tiny.cfg", "yolov3-tiny.weights", 0)
        meta = dn.load_meta("cfg/coco.data")
        r = dn.detect(net,meta,fname)
        for d in r[0:5]:
            print d

