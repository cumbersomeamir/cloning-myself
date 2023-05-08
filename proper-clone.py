!pip3 install numpy sounddevice pyaudio wave openai

import sounddevice as sd
import numpy as np
import wave
import openai
#from elevenlabs import generate, play, set_api_key

message = ""
openai.api_key = "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"

# Configuring audio settings
sample_format = np.int16
channels = 1
rate = 44100
duration = 5  # Duration of recording in seconds
output_file = "output.wav"

print("Recording...")

# Recording audio
audio_data = sd.rec(int(duration * rate), samplerate=rate, channels=channels, dtype=sample_format)
sd.wait()
print(type(audio_data))



print("Recording completed. Saving file...")

# Saving the recorded audio as a WAV file
with wave.open(output_file, 'wb') as wf:
    wf.setnchannels(channels)
    wf.setsampwidth(np.dtype(sample_format).itemsize)
    wf.setframerate(rate)
    wf.writeframes(audio_data.tobytes())

print("File saved as", output_file)



file_path = f"/Users/amirkidwai/Desktop/whisper/lib/python3.8/site-packages/{output_file}"
audio_file = open(file_path, "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript)

transcript = str(transcript)


response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "We are playing a game with my friend. I want you to pretend that you are me - Amir Kidwai. Stay in Character"},
        {"role": "user", "content": transcript}
    ]
    )
    
#messsage = response['choices'][0]['message']['content']

print(response['choices'][0]['message']['content'])




#set_api_key("<94669b2fab0019cfe0c5ac517599f976>")

'''

audio = generate(
    text= str(response['choices'][0]['message']['content']),
    voice="Bella"
)

play(audio, notebook=True)

'''
