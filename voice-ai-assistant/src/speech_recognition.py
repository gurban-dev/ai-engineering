import numpy as np
import soundfile as sf

# Convert recorded speech into text.

# Begin by loading audio, inspecting it waveform, and extracting
# numerical features.

# Then implement and train a speech recognition model.

# Responsibility: Load and audio file
def load_audio(file_path):
    # sf.read() returns two values:
    # audio: the numerical audio samples.
    # sample_rate: the number of audio samples recorded per second.
    audio, sample_rate = sf.read(file_path)

    # Check if the recording has two channels or two separate
    # sound signals: one for the left speaker and one for the
    # right speaker. This is called stereo audio.

    # 'audio references the numerical audio samples loaded from
    # 'file_path'.

    # .ndim is a NumPy attribute that tells us how many dimensions
    # an array has.
    if audio.ndim == 2:
        # Mono audio means there is one channel (one audio signal).
        # Both speakers produce the same signal.
        # E.g. A person speaking into a single microphone.

        # audio.shape -> (16000,)
        
        # Stereo audio uses two signals because it captures sounds
        # from two different perspectives: your left ear and your
        # right ear.

        # Stereo recordings preserve information about the direction
        # from which sounds originate.

        # E.g. Two microphones recording a conversation from different
        #      positions.

        # audio.shape -> (16000, 2)

        # Convert the stereo audio to mono audio by computing the
        # average of the left and right channel samples.

        # axis=1 (axis binded to 1) refers to the columns (2nd dimension)
        # in the NumPy array.
        audio = audio.mean(axis=1)

    # Convert the samples to 32-bit floating-point numbers.

    # 1 bit (a single 0 or 1) is the smallest unit of computer data.
    # 1 bit can be used to represent True or False.

    # 1 byte is equal to 8 bits. E.g. The character "A".

    # Eight individual bits [0 | 1 | 0 | 0 | 0 | 0 | 0 | 1]
    # represents "A".

    # 32 bits is 4 bytes.

    # .astype() converts the NumPy array to data specified
    # (np.float32).

    # np.float32 provides sufficient precision for most audio
    # processing and neural network training.

    # In machine learning, bits are used over bytes because the
    # the data must be broken down more precisely than bytes would
    # allow.
    audio = audio.astype(np.float32)

    # Returns a tuple with two items.
    return audio, sample_rate

def main():
    # ./ means the current directory.
    # ../ means go up one directory level.
    # audio/ means go into the audio directory.
    audio, sample_rate = load_audio("./../audio/file_example_WAV_2MG.wav")

    audio_duration = round(len(audio) / sample_rate, 2)

    print(f"Sample rate: {sample_rate} Hz")
    print(f"Audio duration: {audio_duration} seconds")
    print(f"Audio shape: {audio.shape}")

# Dunder stands for double underscore. These are variables
# and methods built into Python that tells you about the
# internal data of a Python program.

# Examples:
# __name__ reveals how the program was executed.

# If this program was executed by running python speech_recognition.py,
# the dunder variable __name__ would be equal to "__main__".

# __init__() is a dunder method responsible for initialising an
# object's instance variable when you first create that object.
if __name__ == "__main__":
    main()