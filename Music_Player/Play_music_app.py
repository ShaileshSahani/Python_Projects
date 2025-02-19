from tkinter import *
from tkinter import messagebox as m, filedialog
import os
import pygame.mixer as mix
mix.init()
try:
    def load_dic():
        os.chdir(filedialog.askdirectory(title="choose a song folder"))
        tracks = os.listdir()
        if len(tracks) == 0:
            m.showerror(title="No song", message="Folder has no songs")
        else:
            for i in sorted(tracks):
                if i.endswith(".mp3") or i.endswith(".wav") or i.endswith(".m4a"):
                    playlist.insert(END, i)
                else:
                    continue


    def play_song():
        s_selected.config(text=playlist.get(ACTIVE))
        mix.music.load(playlist.get(ACTIVE))
        mix.music.set_volume(0.1)
        mix.music.play()


    def pause():
        mix.music.pause()
        s_selected.config(text="Paused")


    def resume():
        s_selected.config(text=playlist.get(ACTIVE))
        mix.music.unpause()

    def stop():
        mix.music.stop()
        s_selected.config(text="Song Stopped")
    root = Tk()
    root.wm_title("My_Music")
    root.wm_maxsize(600, 257)
    root.wm_minsize(600, 257)
    # Details
    song_info = LabelFrame(root, text="Song Status", height=100, width=346, bd=2, relief="solid", font=10, bg="#636362")
    song_info.place(x=1, y=0)
    s_name = Label(song_info, text="Current Playing: ", font=("ariel", 13, 'bold'))
    s_name.place(x=2, y=20)

    s_selected = Label(song_info, text="< Not Selected >", font=("ariel", 13, 'bold'), bg="#71e1f5")
    s_selected.place(x=150, y=20)

    # Control Button
    con_btn = LabelFrame(root, text="Controls", height=155, width=346, bd=2, relief="solid", font=10, fg="red")
    con_btn.place(x=1, y=101)

    pau_con = Button(con_btn, text="Pause", font=("ariel", 15, 'bold'), bg="#71e1f5", command=pause)
    pau_con.place(x=10, y=10)
    play_con = Button(con_btn, text="Play", font=("ariel", 15, 'bold'), bg="#71e1f5", command=play_song)
    play_con.place(x=95, y=10)
    resume_con = Button(con_btn, text="Resume", font=("ariel", 15, 'bold'), bg="#71e1f5", command=resume)
    resume_con.place(x=160, y=10)
    stop_con = Button(con_btn, text="Stop", font=("ariel", 15, 'bold'), bg="#71e1f5", command=stop)
    stop_con.place(x=265, y=10)

    load_directory = Button(con_btn, text="Load Directory", font=("ariel", 15, 'bold'), bg="#71e1f5", padx=85,
                            command=load_dic)
    load_directory.place(x=10, y=70)

    # Playlist
    directory = LabelFrame(root, text='Playlist', bg="#aeb8b1", height=249, width=249, bd=2, relief="solid", font=10)
    directory.place(x=348, y=0)
    playlist = Listbox(directory, height=11, width=24, font=("ariel", 13, 'bold'), bg="grey", fg="white")
    bar = Scrollbar(directory, orient=VERTICAL)
    playlist.config(yscrollcommand=bar.set)
    bar.pack(side=RIGHT, fill=Y, pady=5)
    bar.config(command=playlist.yview)
    playlist.pack(fill=BOTH, padx=5, pady=5)

    root.mainloop()
except Exception as Er:
    print(Er)
