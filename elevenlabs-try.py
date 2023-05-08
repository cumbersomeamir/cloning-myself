#pip3 install elevenlabs

from elevenlabs import generate, play, set_api_key

# set_api_key("<YOUR_API_KEY>") # Check the guide on how to get a free API key: https://docs.elevenlabs.io/authentication/01-xi-api-key

audio = generate(
    text="Hi! I'm the world's most advanced text-to-speech system, made by elevenlabs.",
    voice="Bella"
)

play(audio, notebook=True)

