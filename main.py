# author: Giorgio
# date: 23.08.2024
# topic: TikTok-Voice-TTS
# version: 1.3

from codecs import BOM_UTF32
import argparse
# the script in the directory
from tiktok_voice import tts, Voice

def main():
    # adding arguments
    parser = argparse.ArgumentParser(description='TikTok TTS')
    parser.add_argument('-t', help='text input')
    parser.add_argument('-v', help='voice selection')
    parser.add_argument('-o', help='output filename', default='output.mp3')
    parser.add_argument('-txt', help='text input from a txt file', type=argparse.FileType('r', encoding="utf-8"))
    parser.add_argument('-play', help='play sound after generating audio', action='store_true')

    args = parser.parse_args()

    # checking if given values are valid
    if not args.t and not args.txt:
        raise ValueError("insert a valid text or txt file")

    if args.t and args.txt:
        raise ValueError("only one input type is possible")
    
    voice: Voice | None = Voice.from_string(args.v)
    if voice == None:
        raise ValueError("no valid voice has been selected")

    # executing script
    if args.t:
        tts(args.t, voice, args.o, args.play)
    elif args.txt:
        tts(args.txt.read(), voice, args.o, args.play)

if __name__ == "__main__":
    main()
