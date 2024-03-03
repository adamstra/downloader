from tkinter import *
from tkinter import ttk
from pytube import YouTube, Playlist
import re


class App(Tk):
    def __init__(self):
        super(App, self).__init__()

        self.title("Video Downlaod")
        self.minsize(400, 400)

        tabControl = ttk.Notebook(self)
        self.video = ttk.Frame(tabControl)
        tabControl.add(self.video, text="Video 🎞")

        self.playlist = ttk.Frame(tabControl)
        tabControl.add(self.playlist, text="Playlist 📄")
        tabControl.pack(expand=1, fill="both")

        self.widgets()

    def widgets(self):
        # La logique
        def videoDownload():
            lien = str(link.get())
            yt = YouTube(lien)
            yt._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
            stream = yt.streams.first()                                                     
            stream.download()
            print("Telechargement terminer")
        
        def playlistDownload():
            lien = str(link.get())
            DOWNLOAD_DIR  = 'C:/Users/lilad/Bureau/playlist'
            p = Playlist(lien)
            print(f'Downloading: {p.title}')
            print('Number of videos in playlist: %s' % len(p.video_urls))
            for tube in p.videos:
                print('downloading : {} with url : {}'.format(tube.title, tube.watch_url))
                tube.streams.\
                filter(type='video', progressive=True, file_extension='mp4').\
                order_by('resolution').desc().first().download(output_path=DOWNLOAD_DIR)            
            # for url in p.video_urls[:-1]:
            #     print (url)

# linksVideo == https://www.youtube.com/watch?v=lq5r5rV8p9M
# linksPlaylist == https://www.youtube.com/playlist?list=PLe3CV80Bij0PJini7nCQ7tZaKxrA3fEax

        # Video
        labelFrame = ttk.LabelFrame(self.video, text="Video link")
        labelFrame.grid(column=0, row=0, padx=8, pady=4)
        label = ttk.Label(labelFrame, text="Enter Your Link:")
        label.grid(column=0, row=0, sticky='W')
        link = StringVar()
        textEdit = ttk.Entry(labelFrame, width=40, textvariable=link)
        textEdit.grid(column=1, row=0)
        btn = ttk.Button(labelFrame, text="Downlaod Video",command=videoDownload)
        btn.grid(column=3, row=0)

        # Playlist
        labelFrame2 = ttk.LabelFrame(self.playlist, text="Playlist link")
        labelFrame2.grid(column=0, row=0, padx=8, pady=4)
        label = ttk.Label(labelFrame2, text="Enter Your Link:")
        label.grid(column=0, row=0, sticky='W')
        link = StringVar()
        textEdit = ttk.Entry(labelFrame2, width=40, textvariable=link)
        textEdit.grid(column=1, row=0)
        btn = ttk.Button(labelFrame2, text="Downlaod Playlist", command=playlistDownload)
        btn.grid(column=3, row=0)


app = App()
app.mainloop()
