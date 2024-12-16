import tkinter as tk
from tkinter.filedialog import askopenfilename

from apkInfo import getPackageName
from shell import installApk
from xml.dom.minidom import parseString

filename = None


def UploadAction(event=None):
    filename = askopenfilename()
    label1['text'] = filename
    getPackageName(filename)


root = tk.Tk()

button1 = tk.Button(text='选择文件', command=UploadAction, bg='brown', fg='white')
button1.pack(padx=2, pady=5)
label1 = tk.Label(text='请选择一个文件')
label1.pack(padx=2, pady=2)
root.mainloop()
