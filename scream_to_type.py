import sounddevice as sd
import numpy as np

def callback(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    print("🔊 Volume:", int(volume_norm))
    if volume_norm > 50:
        print("💥 Scream detected!")

with sd.InputStream(callback=callback):
    print("🎤 Speak (scream) into the mic. Ctrl+C to stop.")
    while True:
        pass
