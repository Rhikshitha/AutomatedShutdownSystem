from tkinter import *
from ctypes import *
import time
import os
print("Started")
root=Tk()
root.title("GUI")
root.geometry('500x500')
cmd='notepad'
class LASTINPUTINFO(Structure):
   _fields_=[
    ('cbSize',c_uint),
    ('dwTime',c_uint)
   ]
def get_idle_duration():
 lastInputInfo=LASTINPUTINFO()
 lastInputInfo.cbSize=sizeof(lastInputInfo)
 windll.user32.GetLastInputInfo(byref(lastInputInfo))
 millis=windll.kernel32.GetTickCount()-lastInputInfo.dwTime
 return millis/1000.0
def update():
 while 1:
  GetLastInputInfo=int(get_idle_duration())
  print(GetLastInputInfo)
  if GetLastInputInfo == 10:
   os.system("shutdown /s /t 1")
  time.sleep(1)
btn_text=StringVar()
btn= Button(root, textvariable=btn_text, fg="blue", command=lambda: update(), bg="#20bebe").place(x=50,y=75)
btn_text.set("Click")
#root.mainloop()
update()

