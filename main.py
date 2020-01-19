from tkinter import *
from pygame import mixer

root = Tk()

mixer.init()

root.geometry('700x400')
root.title("Music Player")

print(TkVersion)

def play_music():
    mixer.music.load("nombrecancion.wav")
    mixer.music.play()

playphoto = PhotoImage(file="play.png")
playbtn = Button(root, image=playphoto)
playbtn.pack()

stopphoto = PhotoImage(file = "stop.png")
stopbtn = Button(root, image=stopphoto)
stopbtn.pack()

pausephoto = PhotoImage(file = "pause.png")
pausebtn = Button(root, image=pausephoto)
pausebtn.pack()

root.mainloop()