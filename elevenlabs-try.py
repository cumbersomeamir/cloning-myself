#pip3 install elevenlabs

import os
from elevenlabs import generate, set_api_key

# set_api_key("<YOUR_API_KEY>") # Check the guide on how to get a free API key: https://docs.elevenlabs.io/authentication/01-xi-api-key

audio = generate(
    text="Hi! I'm the world's most advanced text-to-speech system, made by elevenlabs.",
    voice="Bella"
)

# Save the audio to a file
with open("output.wav", "wb") as f:
    f.write(audio)

# Play the audio file using a command-line tool (assuming the audio format is WAV)
os.system("aplay output.wav")


