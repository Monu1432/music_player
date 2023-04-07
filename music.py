import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Ms Music Player") #application name
canvas.geometry("400x500") # application output screen size
canvas.config(bg= 'black') # output background color of screen
rootpath = "C:\\Users\MONU\Desktop\music file" #paste your music file path in this line
pattern = "*.mp3" #play mp3 music 

mixer.init()
#BUTTON image line 
prev_img = tk.PhotoImage(file = "previous.png")
start_img = tk.PhotoImage(file = "start.png")
pause_img = tk.PhotoImage(file = "pause-squared.png")
naxt_img = tk.PhotoImage(file = "next.png")

def select(): # play music  
    label.config(text= listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop(): #stop music
    mixer.music.stop()
    listBox.select_clear('active')
    
def play_next(): #play next music
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text= next_song_name)
    
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    
    listBox.select_clear(0, "end")
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_prev(): #play previous music
    prev_song = listBox.curselection()
    prev_song = prev_song[0] - 1
    prev_song_name = listBox.get(prev_song)
    label.config(text= prev_song_name)
    
    mixer.music.load(rootpath + "\\" + prev_song_name)
    mixer.music.play()
    
    listBox.select_clear(0, "end")
    listBox.activate(prev_song)
    listBox.select_set(prev_song)
    
    
    
listBox = tk.Listbox(canvas, fg= "cyan", bg="black", width= 100, font = ("poppins", 14)) 
listBox.pack(padx=15, pady=15)

label = tk.Label(canvas, text = "", bg="black", fg="yellow", font=('poppins', 18))
label.pack(pady = 15)

top = tk.Frame(canvas, bg = "black")
top.pack(padx= 10, pady= 5, anchor= "center")

prevButton = tk.Button(canvas, text="Prev", image= prev_img, bg="black", borderwidth= 0, command= play_prev)
prevButton.pack(pady=15, in_ = top, side = "left")

startButton = tk.Button(canvas, text="Play", image= start_img, bg="black", borderwidth= 0, command = select)
startButton.pack(pady=15, in_ = top, side = "left")

pauseButton = tk.Button(canvas, text="stop", image= pause_img, bg="black", borderwidth= 0, command = stop)
pauseButton.pack(pady=15, in_ = top, side = "left")

nextButton = tk.Button(canvas, text="Next", image= naxt_img, bg="black", borderwidth= 0, command=  play_next)
nextButton.pack(pady=15, in_ = top, side = "left")

for root, dirs, files in os.walk(rootpath): # find the directories your given music file in your pc

    for filename in fnmatch.filter(files, pattern):
        listBox.insert("end", filename)
canvas.mainloop()
