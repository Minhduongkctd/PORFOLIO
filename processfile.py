import shutil
import os
import os.path
import datetime
import time
import stat
import sqlite3

conn = sqlite3.connect("file_check.db")


def dropTable():
    conn.execute("DROP TABLE Last_Process")

#dropTable()
def createTable():
    conn.execute("CREATE TABLE if not exists Last_Process(RECORD INTEGER PRIMARY KEY AUTOINCREMENT, FILENAME TEXT, DATETIME REAL);")
createTable()

src_path = "C:\\Users\MinhHang\\Desktop\\srcpath"
dst_path = "C:\\Users\MinhHang\\Desktop\\dstpath"
filelist = os.listdir(src_path)

for testfile in filelist:
    
    
    CheckFile = src_path + "\\" + testfile
    if time.ctime(os.path.getmtime(CheckFile)) not in conn.execute('SELECT * FROM Last_Process'):
        conn.execute('INSERT INTO Last_Process(FILENAME, DATETIME) VALUES(?,?)',(testfile, time.ctime(os.path.getmtime(CheckFile)),))
    
        conn.commit()
                    

def displayTable():

    conn.execute('SELECT * FROM Last_Process')
    
