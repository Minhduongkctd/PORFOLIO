import wx
import os
import shutil
import time
#import wx.lib.buttons as Button

class  MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "UI for File Transfer", size = (800,500))
        P = wx.Panel(self, -1)
        self.CreateStatusBar()

        menu = wx.Menu()
        simple = menu.Append(-1, "Please Select Buttons", "Please Select The Button For File Transfer Purpose!")
        menu.AppendSeparator()
        exit = menu.Append(-1, "Exit", "Selecting This Item Will Exit The Program")
        self.Bind(wx.EVT_MENU, self.OnSimple, simple)
        self.Bind(wx.EVT_MENU, self.OnExit, exit)
        
        menuBar = wx.MenuBar()
        menuBar.Append(menu, "Menu")
        self.SetMenuBar(menuBar)

           
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
        Close_Button = wx.Button(P, -1, 'CLOSE', pos = (380,345), size = (200, 35))
        self.Bind(wx.EVT_BUTTON, self.OnExit, Close_Button)

        #Clear Button
        Clear_Button = wx.Button(P, -1, 'CLEAR_All_TEXT_FIELDS', pos = (380,300), size = (200, 35))
        self.Bind(wx.EVT_BUTTON, self.ClearAll, Clear_Button)

    
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
        
        for file in os.listdir(self.Src_Path):
            src_file = os.path.join(self.Src_Path, file)
            dest_file = os.path.join(self.Dst_Path, file)
            shutil.copyfile(src_file, dest_file)
        
        self.result.WriteText("...All files from Source Folder were transfered to Destination Folder...")
        
    def OnSimple(self, event):
        wx.MessageBox("Please Select The Bottons Below!")

    def OnExit(self, event):
        self.Close()

    def ClearAll(self, event):
        self.srcbox.Clear()
        self.Dstbox.Clear()
        self.result.Clear()
        
if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
