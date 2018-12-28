from tkinter import *
import tkinter.filedialog
from aip import AipFace
import base64
import re
""" 你的 APPID AK SK """
APP_ID = '14939480'
API_KEY = 'LBC6zb6VAy06KbPXMI0XAiEP'
SECRET_KEY = 'bAMXtF4WxkIopIgCSYnBbleINHcanWnT'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)
c=0
root = Tk()
path=[]
def caculate():
    global path
    global lb
    if len(path)==2:
         result=client.match([
    {
        'image': str(base64.b64encode(open(path[0], 'rb').read()), encoding='utf-8'),
        'image_type': 'BASE64',
    },
    {
        'image': str(base64.b64encode(open(path[1], 'rb').read()), encoding='utf-8'),
        'image_type': 'BASE64',
    }])
    lb.config(text = "相似度："+ re.findall("'score': (.+), 'face_list'",str(result))[0])

def xz():
    global c
    global path
    filename = tkinter.filedialog.askopenfilename()
    if len(filename)>0 and c<=1:
        path.append(filename)
        c+=1
        print(c,filename)

lb = Label(root,text = '')
lb.pack()
btn = Button(root,text="选择图片",command=xz)
btn.pack()
bt= Button(root,text="计算相似度",command=caculate)
bt.pack()
lb = Label(root,text = '相似度：')
lb.pack()
root.mainloop()
