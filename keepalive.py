import numpy as np
import sounddevice as sd
from threading import Timer





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