from appJar import gui

app = gui()
# Add an audio player widget to the GUI
player = app.addAudioPlayer()

# Load an audio file into the player
player.setFile("audio.mp3")

# Add buttons to control playback
app.addButton("Play", player.play)
app.addButton("Pause", player.pause)
app.addButton("Stop", player.stop)

app.go()
