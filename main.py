import vlc
media = vlc.MediaPlayer("http://direct.franceinter.fr/live/franceinter-midfi.mp3")
media.play()

while True:
    pass