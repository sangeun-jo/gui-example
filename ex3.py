from tkinter import *

tk = Tk()

counter = 0

def clicked():
    global counter
    counter += 1
    label1['text'] = '버튼 클릭 수: ' + str(counter)
    

def reset():
    global counter
    counter = 0
    label1['text'] = '옆에 버튼이 있습니다.'

tk.title('GUI 예제')

label1 = Label(tk, text='옆에 버튼이 있습니다.', fg='blue', font=20)
label1.pack(side=LEFT, padx=10, pady=10)

button3 = Button(tk, text='클릭해 보세요.', bg='green', font=15, width=30, height=5, command= clicked)
button3.pack(side=LEFT, padx=10, pady=10)

button4 = Button(tk, text='reset', bg='red', width=30, height=5, font=15, command=reset)
button4.pack(side=LEFT, padx=10, pady=10)
tk.mainloop()
