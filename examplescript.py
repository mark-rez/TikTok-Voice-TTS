# author: GiorDior aka Giorgio
# date: 12.06.20023
# topic: TikTok-Voice-TTS
# version: 1.0

from tiktokvoice import *

text = "I am a hero!"
voice = "en_us_006" # all possible voices can be found here

# arguments:
#   - input text
#   - vocie which is used for the audio
#   - output file name
#   - play sound after generating the audio
tts(text, voice, "output.mp3", play_sound=True)
