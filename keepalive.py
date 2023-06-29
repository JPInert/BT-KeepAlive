import sys
import numpy as np
import sounddevice as sd
from threading import Timer
import pystray
from pystray import MenuItem as item
from PIL import Image
import subprocess
import os 

def play_silent_audio():
    silent_duration = 1  # Duration of the silent audio segment in seconds
    samplerate = 44100  # Specify the desired samplerate for the audio

    # Generate a silent audio array
    silent_samples = np.zeros(int(silent_duration * samplerate), dtype=np.float32)

    # Play the silent audio
    sd.play(silent_samples, samplerate=samplerate, blocking=False)

    # Schedule the next playback after 10 minutes
    t = Timer(600, play_silent_audio)
    t.start()

play_silent_audio()

# Embed icon and enable relative paths
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Kill process on exit
def exit_action(icon, item):
    icon.stop()
    subprocess.call(["taskkill", "/f", "/im", "btka.exe"])

# Include icon image
icon_image = Image.open(resource_path("icon.ico"))
menu = (item('Exit', exit_action),)

# Create the system tray icon
icon = pystray.Icon("BT KeepAlive", icon_image, "BT KeepAlive", menu)
icon.run()