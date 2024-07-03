# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

## Audio record and play
import pyaudio
import wave

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 5
filename = "output.wav"

# ********* Recording start *********
p = pyaudio.PyAudio()  # Create an interface to PortAudio
print('Recording')
stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording')
# ********* Recording done *********

# ********* Show figures *********
framesJoined = b''.join(frames)
amplitude = np.frombuffer(framesJoined, np.int16)
plt.plot(amplitude,label='Original')

#  perform filtration
sos = signal.butter(5, [1000, 2000], 'bp', fs=fs, output='sos')
filteredAudio = signal.sosfilt(sos, amplitude)
plt.plot(filteredAudio,label='filtered')
plt.legend()
plt.show()
# ********* show figures end *********

# ********* Save Record as wav *********
ampbytes = bytes(amplitude)
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(ampbytes)
wf.close()
# ********* Save Record as wav end *********

# ********* Output audio *********
print('Play audio')
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=channels,
                rate=fs,
                frames_per_buffer=2048,
                output=True
                )

# Convert to integer for audio out
filteredAudioInt = [0] * len(filteredAudio)
for i in range(0,len(filteredAudio)):
    filteredAudioInt[i] = int(filteredAudio[i])

print('Play audio Original')
amplitude = np.array(amplitude)
stream.write(amplitude.astype(np.int16).tostring())

print('Play audio filtered')
filteredAudioInt = np.array(filteredAudioInt)
stream.write(filteredAudioInt.astype(np.int16).tostring())

stream.close()
p.terminate()
# ********* Output audio done *********
