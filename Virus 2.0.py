from operator import truediv
from tkinter import * #import library "tkinter"
from tkinter import messagebox
import subprocess
import time
import os
from PIL import Image, ImageTk
import ctypes
import random



def btn_fc(btn):
    btn.place_configure(relx=random.random(), rely=random.random())


def btn_no(event=None):
    btn.place_forget()
    text2.place_forget()
    btn1.place_forget()
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))
    btn3.place(relx=.5, rely=.9, anchor='c')
    text3.place(relx=.5, rely=.5, anchor='c')
    btn2.place(relx=.5, rely=.7, anchor='c')

    root.configure(bg='black')

def GG(event=None):
    def change_wallpaper(new_image_path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, new_image_path, 0)


root=Tk() #create window
root.title("программа") #name window

root.resizable(width=False, height=False)
root.geometry('1500x1024')

new_wallaper_path = ('c59ad2bd4ad2fbacd04017debc679ddb.jpg')

text2=Label(text='Хочешь прикол?', font=(50))
text2.place(relx=.5, rely=.5, anchor='c')


btn=Button(text='да', bg='Yellow', width=15, heigh=2, command=btn_fc, font=(50))
btn.place(relx=.5, rely=.7, anchor="c")
btn.bind('<Enter>', lambda event: btn_fc(btn))


btn1=Button(text='нет', bg='Black', fg='White', width=15, height=2, font=(50), command=btn_no)
btn1.place(relx=.5, rely=.9, anchor='c')


text3=Label(text='Уверен?', font=(70), bg='black', fg='red')


btn2=Button(text='Уверен', bg='red', fg='black', width=15, height=2, font=(50), command=GG)
btn3=Button(text='Все таки хочу', bg='red', fg='black', command=btn_fc, width=15, height=2, font=(50))


root.mainloop()