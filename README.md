# TikTok Voice TTS

This is a simple Python program that gives you an `.mp3` file including the given text input which is spoken by one of the TikTok voices.

I thank all people that use this for their project. I love to contribute to the community. However, please credit me by using the GitHub project link.

## Usage
To use this program, you need an internet connection, python 3.6+ and all of the required packages installed.
To install the required packages, run: `pip3 install -r requirements.txt`

### Create audio from file
1. Make sure you have your text in the file plaintext.
2. Run `py main.py -txt FILENAME.txt -v VOICENAME` (see voices below)

Only latin characters are supported.

### Create audio from argument
1. Run `py main.py -t TEXT -v VOICENAME` (see voices below)

You can have non-latin characters (as long as it has a TTS supported voice).

### Create audio in python script
1. Put the file folder/package `tiktok_voice` into your directory.
2. Import the text-to-speech function and the voices with `from tiktok_voice import tts, Voice`.
3. Execute `tts(TEXT, VOICE, OUTPUTFILENAME, PLAYSOUND)` in your code. 

I provided an [example script](https://github.com/GiorDior/TikTok-Voice-TTS/blob/main/example_script.py) which shows how the tts function could be used in a script.

## Voices
List of every voice and its designation:

| Name                 |
| -------------------- |
| GHOSTFACE            |
| CHEWBACCA            |
| C3PO                 |
| STITCH               |
| STORMTROOPER         |
| ROCKET               |
| EN_AU_FEMALE_1       |
| EN_AU_MALE_1         |
| EN_UK_MALE_1         |
| EN_UK_MALE_2         |
| EN_US_FEMALE_1       |
| EN_US_FEMALE_2       |
| EN_US_MALE_1         |
| EN_US_MALE_2         |
| EN_US_MALE_3         |
| EN_US_MALE_4         |
| FR_MALE_1            |
| FR_MALE_2            |
| DE_FEMALE            |
| DE_MALE              |
| ES_MALE              |
| ES_MX_MALE           |
| BR_FEMALE_1          |
| BR_FEMALE_2          |
| BR_FEMALE_3          |
| BR_MALE              |
| ID_FEMALE            |
| JP_FEMALE_1          |
| JP_FEMALE_2          |
| JP_FEMALE_3          |
| JP_MALE              |
| KR_MALE_1            |
| KR_FEMALE            |
| KR_MALE_2            |
| EN_FEMALE_ALTO       |
| EN_MALE_TENOR        |
| EN_FEMALE_WARMY_BREEZE |
| EN_MALE_SUNSHINE_SOON |
| EN_MALE_NARRATION    |
| EN_MALE_FUNNY        |
| EN_FEMALE_EMOTIONAL  |

## Samples

You can find samples of all voices in [/samples/](https://github.com/GiorDior/TikTok-Voice-TTS/tree/main/samples)

## Credits
- [oscie](https://github.com/oscie57/tiktok-voice) for giving me the idea for this project
