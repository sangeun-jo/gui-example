from tkinter import *

tk = Tk()

def event():
    button['text'] = '버튼누름!'

button = Button(tk, text='함수 실행', command=event)
button2 = Button(tk, text='버튼2')

button.pack(side=LEFT, padx=10, pady=10)
button2.pack(side=RIGHT, padx=10, pady=10)
tk.mainloop()
