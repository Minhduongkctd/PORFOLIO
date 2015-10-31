import shutil
import os
import os.path
import datetime
import time
import stat


src_path = "C:\\Users\MinhHang\\Desktop\\srcpath"
dst_path = "C:\\Users\MinhHang\\Desktop\\dstpath"
filelist = os.listdir(src_path)
fileStat = os.stat(src_path)


nowStamp = time.time()
dayStarted = time.time() - (24*60*60)



for testfile in filelist:
    CheckFile = src_path + "\\" + testfile
    
    if os.stat(CheckFile).st_mtime > dayStarted:
        print ("coping " + CheckFile)
        destFile = dst_path + "\\" + testfile
        shutil.copy(CheckFile,destFile)
        

