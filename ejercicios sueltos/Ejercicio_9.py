import _thread


def scrip_thread(thread, num):
    for i in range(1, num+1):
        print("thread", thread, ":", i)


try:
    _thread.start_new_thread(scrip_thread, (1, 3))
    
except:
    print("error")





