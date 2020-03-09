from tkinter import *

def save_info():
    t1_info = t1.get()
    t2_info = t2.get()
    print(t1_info, t2_info)

    file = open("save.json", "w")
    file.write(t1_info)
    file.write(t2_info)
    file.close()

    t1.delete(0, END)
    t2.delete(0, END)



screen = Tk()
screen.geometry("400x300+10+10")
screen.title("python gui save in jason file")


heading = Label(text="PYTHON GUI SAVE IN JSON FILE")
heading.pack()

lbl1 = Label(text='ANIMAL / BIRD')
lbl2 = Label(text='NAME')
lbl1.place(x=100, y=50)
lbl2.place(x=100, y=100)

lbl1 = StringVar()
lbl2 = StringVar()

t1 = Entry()
t1.place(x=200, y=50)
t2 = Entry()
t2.place(x=200, y=100)

save = Button(screen, text="SAVE", command=save_info)
save.place(x=100, y=150)

Exit = Button(screen, text="EXIT",command=screen.quit)
Exit.place(x=150, y=150)
screen.mainloop()