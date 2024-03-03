from tkinter import *
from tkinter import ttk
from pytube import YouTube

App = Tk()
App.title = ("Video Downlaod")
App.minsize(400,400)

tabControl = ttk.Notebook()
video = ttk.Frame(tabControl)
tabControl.add(video, text="Video 🎞")

playlist = ttk.Frame(tabControl)
tabControl.add(playlist, text="Playlist 📄")
tabControl.pack(expand=1, fill="both")

def videoDownload():
      lien = str(link.get())
      yt = YouTube(lien)
      stream = yt.streams.first()
      stream.download()
      print("Telechargement terminer")

#Video
labelFrame = ttk.LabelFrame(video, text="Video link")
labelFrame.grid(column=0, row=0, padx=8, pady=4)
label = ttk.Label(labelFrame, text="Enter Your Link:")
label.grid(column=0, row=0, sticky='W')
link = StringVar()
textEdit = ttk.Entry(labelFrame, width=40, textvariable=link)
textEdit.grid(column=1, row=0)
btn = ttk.Button(labelFrame, text="Downlaod Video",command=videoDownload)
btn.grid(column=3, row=0)

# Playlist
labelFrame2 = ttk.LabelFrame(playlist, text="Playlist link")
labelFrame2.grid(column=0, row=0, padx=8, pady=4)
label = ttk.Label(labelFrame2, text="Enter Your Link:")
label.grid(column=0, row=0, sticky='W')
link = StringVar()
textEdit = ttk.Entry(labelFrame2, width=40, textvariable=link)
textEdit.grid(column=1, row=0)
btn = ttk.Button(labelFrame2, text="Downlaod Playlist")
btn.grid(column=3, row=0)



App.mainloop()