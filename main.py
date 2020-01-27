import os
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
from pygame import mixer
import time

root = Tk()

#Create the menubar
menubar = Menu(root)
root.config(menu=menubar)

playlist = []

#Select file from your hard drive
def browse_file():
    global filename
    filename = filedialog.askopenfilename()
    add_to_playlist(filename)

def add_to_playlist(f):
    f = os.path.basename(f)
    i = 0
    LB.insert(i, f)
    playlist.insert(i, filename)
    i = i + 1

#Create the submenu File
submenu = Menu(menubar)
menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label = "Open", command = browse_file)

#Message from about_us window
def about_us():
    tkinter.messagebox.showinfo('About us','Music player made by Salvador Delgado Arroyo')

#Creat the submenu Help
submenu = Menu(menubar)
menubar.add_cascade(label = "Help", menu=submenu)
submenu.add_command(label = "About us", command = about_us)

mixer.init()    #initializer of mixer

root.geometry('900x300')    #dimension of the window
root.title("Music Player")  #window title

leftframe = Frame(root)
leftframe.pack(side = LEFT, padx = 30)

LB = Listbox(leftframe)
LB.pack()

addbtn = Button(leftframe, text = "+ Add", command = browse_file)
addbtn.pack(side = LEFT, padx = 20, pady = 10)

delbtn = Button(leftframe, text = "- Del")
delbtn.pack(pady = 10)

#Function to play music
def play_music():
    global paused

    if paused:
        mixer.music.unpause()
        statusbar['text'] = os.path.basename(filename) + ' ' + 'resumed'
        paused = FALSE
    else:
        try:
            stop_music()
            time.sleep(1)
            selected_song = int(LB.curselection()[0])
            print(selected_song)
            play_it = playlist[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            a = mixer.Sound(play_it)
            total_length = a.get_length()
            mins, secs = divmod(total_length,60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{02d}'.format(mins,secs)
            statusbar['text'] = 'Playing' + ' ' + os.path.basename(play_it) + timeformat
        except:
            tkinter.messagebox.showerror('File not found','We could not find the file. Please try again.')
        
#Function to stop music
def stop_music():
    mixer.music.stop()
    statusbar['text'] = os.path.basename(filename) + ' ' + 'stopped'

paused = FALSE

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