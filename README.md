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
| ----------------------------- |
| GHOSTFACE                     |
| CHEWBACCA                     |
| C3PO                          |
| STITCH                        |
| STORMTROOPER                  |
| ROCKET                        |
| MADAME_LEOTA                  |
| GHOST_HOST                    |
| PIRATE                        |
| AU_FEMALE_1                   |
| AU_MALE_1                     |
| UK_MALE_1                     |
| UK_MALE_2                     |
| US_FEMALE_1                   |
| US_FEMALE_2                   |
| US_MALE_1                     |
| US_MALE_2                     |
| US_MALE_3                     |
| US_MALE_4                     |
| MALE_JOMBOY                   |
| MALE_CODY                     |
| FEMALE_SAMC                   |
| FEMALE_MAKEUP                 |
| FEMALE_RICHGIRL               |
| MALE_GRINCH                   |
| MALE_DEADPOOL                 |
| MALE_JARVIS                   |
| MALE_ASHMAGIC                 |
| MALE_OLANTERKKERS             |
| MALE_UKNEIGHBOR               |
| MALE_UKBUTLER                 |
| FEMALE_SHENNA                 |
| FEMALE_PANSINO                |
| MALE_TREVOR                   |
| FEMALE_BETTY                  |
| MALE_CUPID                    |
| FEMALE_GRANDMA                |
| MALE_XMXS_CHRISTMAS           |
| MALE_SANTA_NARRATION          |
| MALE_SING_DEEP_JINGLE         |
| MALE_SANTA_EFFECT             |
| FEMALE_HT_NEYEAR              |
| MALE_WIZARD                   |
| FEMALE_HT_HALLOWEEN           |
| FR_MALE_1                     |
| FR_MALE_2                     |
| DE_FEMALE                     |
| DE_MALE                       |
| ES_MALE                       |
| ES_MX_MALE                    |
| BR_FEMALE_1                   |
| BR_FEMALE_2                   |
| BR_FEMALE_3                   |
| BR_MALE                       |
| BP_FEMALE_IVETE               |
| BP_FEMALE_LUDMILLA            |
| PT_FEMALE_LHAYS               |
| PT_FEMALE_LAIZZA              |
| PT_MALE_BUENO                 |
| ID_FEMALE                     |
| JP_FEMALE_1                   |
| JP_FEMALE_2                   |
| JP_FEMALE_3                   |
| JP_MALE                       |
| KR_MALE_1                     |
| KR_FEMALE                     |
| KR_MALE_2                     |
| JP_FEMALE_FUJICOCHAN          |
| JP_FEMALE_HASEGAWARIONA       |
| JP_MALE_KEIICHINAKANO         |
| JP_FEMALE_OOMAEAIIKA          |
| JP_MALE_YUJINCHIGUSA          |
| JP_FEMALE_SHIROU              |
| JP_MALE_TAMAWAKAZUKI          |
| JP_FEMALE_KAORISHOJI          |
| JP_FEMALE_YAGISHAKI           |
| JP_MALE_HIKAKIN               |
| JP_FEMALE_REI                 |
| JP_MALE_SHUICHIRO             |
| JP_MALE_MATSUDAKE             |
| JP_FEMALE_MACHIKORIIITA       |
| JP_MALE_MATSUO                |
| JP_MALE_OSADA                 |
| SING_FEMALE_ALTO              |
| SING_MALE_TENOR               |
| SING_FEMALE_WARMY_BREEZE      |
| SING_MALE_SUNSHINE_SOON       |
| SING_FEMALE_GLORIOUS          |
| SING_MALE_IT_GOES_UP          |
| SING_MALE_CHIPMUNK            |
| SING_FEMALE_WONDERFUL_WORLD   |
| SING_MALE_FUNNY_THANKSGIVING  |
| MALE_NARRATION                |
| MALE_FUNNY                    |
| FEMALE_EMOTIONAL              |

## Samples

You can find samples of all voices in [/samples/](https://github.com/GiorDior/TikTok-Voice-TTS/tree/main/samples)

## Credits
- [oscie](https://github.com/oscie57/tiktok-voice) for giving me the idea for this project

## License
```
MIT License

Copyright (c) 2024 Mark Reznikov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```