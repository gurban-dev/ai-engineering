import numpy as np
import soundfile as sf

# Convert recorded speech into text.

# Begin by loading audio, inspecting it waveform, and extracting
# numerical features.

# Then implement and train a speech recognition model.

def load_audio(file_path):
    # sf.read() returns two values:
    # audio: the numerical audio samples.
    # sample_rate: the number of audio samples recorded per second.
    audio, sample_rate = sf.read(file_path)