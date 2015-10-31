import wx
import os, os.path
import shutil
import time, datetime, stat
import processfile
import sqlite3

conn = sqlite3.connect("file_check.db")
#import wx.lib.buttons as Button

class  MyFrame(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "UI for File Transfer", size = (900,600))
        P = wx.Panel(self, -1)
        self.CreateStatusBar()

        menu = wx.Menu()
        simple = menu.Append(-1, "Please Select Buttons", "Please Select The Button For File Transfer Purpose!")
        menu.AppendSeparator()
        toexit = menu.Append(-1, "Exit", "Selecting This Item Will Exit The Program")
        self.Bind(wx.EVT_MENU, self.OnSimple, simple)
        self.Bind(wx.EVT_MENU, self.OnExit, toexit)
        
        menuBar = wx.MenuBar()
        menuBar.Append(menu, "Menu")
        self.SetMenuBar(menuBar)
        

        
        
        
        #Add data to the list control
        #self.fillListCtrl()
        self.listCtrl = wx.ListCtrl(P, size=(570, 300), pos=(20,200), style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        
        #Add columns to listCtrl
        self.listCtrl.InsertColumn(0, 'RECORD', wx.LIST_FORMAT_CENTRE, width = 60)
        self.listCtrl.InsertColumn(1, 'FILENAME', wx.LIST_FORMAT_CENTRE, width = 180)
        self.listCtrl.InsertColumn(2, 'DATETIME', wx.LIST_FORMAT_CENTRE, width = 250)
        
        #1st This button for source:
        Src_b = wx.Button(P, -1, '    Source Forder    ', pos = (20,20))
        self.srcbox = wx.TextCtrl(P, -1, "", pos = (140,20), size =(450,25))
        self.srcbox.SetInsertionPoint(0)
        self.Bind(wx.EVT_BUTTON, self.ChangeSource, Src_b)
        self.Src_Path = " "
        self.result = wx.TextCtrl(P, -1, "", pos = (20,140), size =(570,40))

        
        
        #2nd This button for destination:
        Dst_b = wx.Button(P, -1, 'Destination Folder', pos = (20, 60))
        self.Dstbox = wx.TextCtrl(P, -1, "", pos = (140,60), size = (450,25))
        self.Dstbox.SetInsertionPoint(0)
        self.Bind(wx.EVT_BUTTON, self.ChangeDestination, Dst_b)
        self.Dst_Path = " " 
        
        #3rd This button for Transfer files:
        Trans_b = wx.Button(P, -1, '  Click Here to Transfer file...  ', pos = (20,100))
        self.Bind(wx.EVT_BUTTON, self.ActionTransfer, Trans_b)
        
        #Close Button
        Close_Button = wx.Button(P, -1, 'CLOSE', pos = (680,310), size = (160, 35))
        self.Bind(wx.EVT_BUTTON, self.OnExit, Close_Button)

        #Clear Button
        Clear_Button = wx.Button(P, -1, 'CLEAR_All_TEXT_FIELDS', pos = (680,270), size = (160, 35))
        self.Bind(wx.EVT_BUTTON, self.ClearAll, Clear_Button)
        #Recording To DataBase Button
        Record_Button = wx.Button(P, -1, 'RECORDING_TO_DATABASE', pos = (680, 230), size = (160, 35))
        #self.Bind(wx.EVT_BUTTON, self.function, Record_Button)

        #Create table Button
        Create_Table = wx.Button(P, -1, 'CREATE TABLE', pos = (680, 150), size = (160, 35))
        self.Bind(wx.EVT_BUTTON, self.createTable, Create_Table)
        #Drop table Button
        Drop_Table = wx.Button(P, -1, 'DROP TABLE', pos = (680, 190), size = (160, 35))
        self.Bind(wx.EVT_BUTTON, self.dropTable, Drop_Table)
    
     #This function define for source button       
    def ChangeSource(self, event):
        
        self.Src_Path = wx.DirSelector("Please Choose a Folder")
        self.srcbox.WriteText(self.Src_Path) #this WriteText is to write in the path

       
     #This define for destination button
    def ChangeDestination(self, event):
        
        self.Dst_Path = wx.DirSelector("Please Choose a Folder")
        self.Dstbox.WriteText(self.Dst_Path)
        
     #This define for action transfer button
    def ActionTransfer(self, event):
        
        for nfile in os.listdir(self.Src_Path):
            src_file = os.path.join(self.Src_Path, nfile)
            dest_file = os.path.join(self.Dst_Path, nfile)
            shutil.copyfile(src_file, dest_file)
            
        self.result.WriteText("...All files from Source Folder were transfered to Destination Folder...")
     #This function define for recording
    def RecordData(self, event):
        src_path = "C:\\Users\MinhHang\\Desktop\\srcpath"
        filelist = os.listdir(dst_path)
        for testfile in filelist:
            if time.ctime(os.path.getmtime(CheckFile)) not in conn.execute('SELECT DATETIME FROM Last_Process'):
                conn.execute('INSERT INTO Last_Process(FILENAME, DATETIME) VALUES(?,?)',(testfile, time.ctime(os.path.getmtime(CheckFile)),))
                conn.commit()


    def dropTable(self, event):

        
        conn.execute("DROP TABLE Last_Process")
        
      

    def createTable(self, event):
        #P = wx.Panel(self, -1)
        conn.execute("CREATE TABLE if not exists Last_Process(RECORD INTEGER PRIMARY KEY AUTOINCREMENT, FILENAME TEXT, DATETIME REAL);")


    def OnSimple(self, event):
        wx.MessageBox("Please Select The Bottons Below!")

    def OnExit(self, event):
        self.Close()

    def ClearAll(self, event):
        self.srcbox.Clear()
        self.Dstbox.Clear()
        self.result.Clear()
        self.listCtrl.Clear()
        
if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
