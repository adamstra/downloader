from tkinter import *
from tkinter import ttk
from pytube import YouTube
import os


app = Tk()
app.geometry("500x500")
app.title("Downloader youtube")


def download():
    lien = link.get()
    yt = YouTube(str(lien))
    stream = yt.streams.get_by_itag(22)
    stream.download()


# tabControl = ttk.Notebook()
# video = ttk.Frame(tabControl)
# tabControl.add(video, text="Video")
# playtlist = ttk.Frame(tabControl)
# tabControl.add(playtlist, text="Playlist")
# tabControl.pack(expan=1, fill="both")

label = ttk.Label(app, text="Lien :", font=('Arial', 20, 'bold'))
label.grid(column=0, row=0)

link = StringVar()
input = ttk.Entry(app, width=50, textvariable=link)
input.grid(column=1, row=0)

btn = ttk.Button(app, text="Download", command=download)
btn.grid(column=3, row=0)

bar = ttk.Progressbar(app, orient=HORIZONTAL, length=300)
bar.grid(column=1, row=1)


app.mainloop()
