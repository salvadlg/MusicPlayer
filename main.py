import os
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
from pygame import mixer

root = Tk()

#Create the menubar
menubar = Menu(root)
root.config(menu=menubar)

#Select file from your hard drive
def browse_file():
    global filename
    filename = filedialog.askopenfilename()

#Create the submenu File
submenu = Menu(menubar)
menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label = "Open", command = browse_file)
submenu.add_command(label = "New Playlist")

#Message from about_us window
def about_us():
    tkinter.messagebox.showinfo('About us','Music player made by Salvador Delgado Arroyo')

#Creat the submenu Help
submenu = Menu(menubar)
menubar.add_cascade(label = "Help", menu=submenu)
submenu.add_command(label = "About us", command = about_us)

mixer.init()    #initializer of mixer

root.geometry('700x300')    #dimension of the window
root.title("Music Player")  #window title

#Function to play music
def play_music():
    try:
        paused  #checks if the 'paused' variable is initilized
    except NameError:   #if it's not initialized then executes the code
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = 'Playing' + ' ' + os.path.basename(filename)
        except:
            tkinter.messagebox.showinfo('File not found','We could not find the file. Please try again.')
    else:   #if it's initialized then executes the else code
        mixer.music.unpause()
        statusbar['text'] = os.path.basename(filename) + ' ' + 'resumed'

#Function to stop music
def stop_music():
    mixer.music.stop()
    statusbar['text'] = os.path.basename(filename) + ' ' + 'stopped'

#Funcion to pause music
def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = os.path.basename(filename) + ' ' + 'paused'

#Function to set volume 
def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)

def rewind_music():
    play_music()

def forward_music():

muted = FALSE

#Function to mute music
def mute_music():
    global muted 
    if muted:
        mixer.music.set_volume(0.5)
        soundbtn.configure(image=soundPhoto)
        scale.set(50)
        muted = FALSE
    else:
        mixer.music.set_volume(0)
        soundbtn.configure(image=mutePhoto)
        scale.set(0)
        muted = TRUE

#mute button
mutePhoto = PhotoImage(file='mute.png')
soundPhoto = PhotoImage(file='sound.png')
soundbtn = Button(root, image=soundPhoto, command=mute_music)
soundbtn.pack()

#rewind button
rewindphoto = PhotoImage(file = "rewind.png")
rewindbtn = Button(root, image=rewindphoto, command = rewind_music)
rewindbtn.pack(side = LEFT, padx = 10)

#play button
playphoto = PhotoImage(file="play.png")
playbtn = Button(root, image=playphoto, command = play_music)
playbtn.pack(side = LEFT, padx = 10)

#forward button
forwardphoto = PhotoImage(file = "fast-forward.png")
forwardbtn = Button(root, image=forwardphoto, command = forward_music)
forwardbtn.pack(side = LEFT, padx = 10)

#stop button
stopphoto = PhotoImage(file = "stop.png")
stopbtn = Button(root, image=stopphoto, command = stop_music)
stopbtn.pack(side = LEFT, padx = 10)

#pause button
pausephoto = PhotoImage(file = "pause.png")
pausebtn = Button(root, image=pausephoto, command = pause_music)
pausebtn.pack(side = LEFT, padx = 10)

#volume bar
scale = Scale(root, from_ = 0, to = 100, orient = HORIZONTAL, command = set_vol)
scale.set(50)
mixer.music.set_volume(0.5)
scale.pack(pady=70)

#current status of the music
statusbar = Label(root, relief=SUNKEN, anchor = W)
statusbar.pack(side=BOTTOM, fill = X)

root.mainloop()