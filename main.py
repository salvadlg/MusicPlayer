from tkinter import *

root = Tk()
root.geometry('700x400')
root.title("Music Player")
root.iconbitmap("headphone.gif")

print(TkVersion)

photo = PhotoImage(file="play.gif")
btn = Button(root, image=photo)
btn.pack()


root.mainloop()