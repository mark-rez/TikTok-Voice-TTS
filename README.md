# TikTok Voice TTS

This is a simple Python program that gives you an `.mp3` file including the given text input which is spoken by one of the TikTok voices.

I thank all people that use this for their project. I love to contribute to the community. However, please credit me by using the GitHub project link.

## Usage

To use this program, you need an internet connection, python 3.6+ and all of the required packages installed.
To install the required packages, run: `pip3 install -r requirements.txt`

### Create audio from file
1. Make sure you have your text in plaintext. You can name it anything
2. Run `py main.py -txt FILENAME.txt -v VOICENAME` (see voices below)

Only latin characters are supported.

### Create audio from argument
1. Run `py main.py -t TEXT -v VOICENAME` (see voices below)

You can have non-latin characters (as long as it has a TTS supported voice).

### Create audio in python script
1. Put the file `tiktokvoice.py` into your directory.
2. Import the text-to-speech function with `from tiktokvoice import tts`.
3. Execute `tts(TEXT, VOICENAME, OUTPUTFILENAME, PLAYSOUND)` in your code. 

I provided an [example script](https://github.com/GiorDior/TikTok-Voice-TTS/blob/main/examplescript.py) which shows how the tts function could be used in a script.

## Supported languages:
List of every voice and its designation: [voices](https://github.com/oscie57/tiktok-voice/wiki/Voice-Codes)

- Portuguese (Brazil)
- German
- English (Australia)
- English (United Kingdom)
- English (United States)
- English (Disney)
- Spanish
- Spanish (Mexico)
- French
- Indonesian
- Japanese
- Korean

## Samples

You can find samples of all voices in [/samples/](https://github.com/GiorDior/TikTok-Voice-TTS/tree/main/samples)

## Credits
- [oscie](https://github.com/oscie57/tiktok-voice) for giving me the idea for this project
