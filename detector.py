import sys, os
import time
import threading
import Queue

sys.path.append(os.path.join(os.getcwd(),'python/'))


import darknet as dn
import pdb
import cap

in_q = Queue.Queue(maxsize = 100)
out_q = Queue.Queue(maxsize = 100)

net = dn.load_net("cfg/yolov3-tiny.cfg", "yolov3-tiny.weights", 0)
meta = dn.load_meta("cfg/coco.data")

        
#-------------------
# predict_thread
#-------------------
def predict_thread(p1):
    global in_q
    while True:
    
        fname = in_q.get()
        if fname != None and len(fname) > 0:
            t1 = time.time()
            r = dn.detect(net,meta,fname)
            t2 = time.time()
            print '--------------------------------------'
            print p1,fname,t2-t1
            for d in r[:5]:
                print d
            print '--------------------------------------'                
            #out_q.put(r)
        else:
            print p1,' waiting for in_q ...'
#-------------------------
# main
#-------------------------
if __name__ == "__main__":    

    dn.set_gpu(0)

    t1 = threading.Thread(target=predict_thread,args=('predict_1',)).start()
    t2 = threading.Thread(target=predict_thread,args=('predict_2',)).start()
    #t3 = threading.Thread(target=predict_thread,args=('predict_3',)).start()
    #t4 = threading.Thread(target=predict_thread,args=('predict_4',)).start()
    #t5 = threading.Thread(target=predict_thread,args=('predict_5',)).start()
    #t6 = threading.Thread(target=predict_thread,args=('predict_6',)).start()
    #t7 = threading.Thread(target=predict_thread,args=('predict_7',)).start()
    #t8 = threading.Thread(target=predict_thread,args=('predict_8',)).start()

    while True:
        fname = 'data/' + str(time.time()) + '.jpg'
        ret,x,y = cap.cap(fname,640,480)
        if ret == 0:
            in_q.put(fname)
            print 'save file:',fname
        time.sleep(1.2)

        
