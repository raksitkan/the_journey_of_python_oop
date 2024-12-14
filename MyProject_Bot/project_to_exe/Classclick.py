import win32api,win32gui,win32con
class click:
    def __init__(self,windowsname):
        self.windowsname = windowsname
    def gethwid(self):
        hwid = win32gui.FindWindow('LDPlayerMainFrame',self.windowsname)
        childs = win32gui.FindWindowEx(hwid,None,'RenderWindow','TheRender')
        return childs
    def getchromeid(self):
        hwid = win32gui.FindWindow('Chrome_WidgetWin_1',self.windowsname)
        return hwid  
    
    def control_click(self,hwid,x,y):
        l_param = win32api.MAKELONG(x,y)
        win32gui.SendMessage(hwid,win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,l_param)
        win32gui.SendMessage(hwid,win32con.WM_LBUTTONUP,win32con.MK_LBUTTON,l_param)