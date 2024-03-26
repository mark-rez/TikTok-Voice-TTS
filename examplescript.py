from tiktokvoice import tts

text = 'Tangerines are smaller and less rounded than the oranges. The taste is considered less sour, as well as sweeter and stronger, than that of an orange. A ripe tangerine is firm to slightly soft, and pebbly-skinned with no deep grooves, as well as orange in color. The peel is thin, with little bitter white mesocarp. All of these traits are shared by mandarins generally. Peak tangerine season lasts from autumn to spring. Tangerines are most commonly peeled and eaten by hand. The fresh fruit is also used in salads, desserts and main dishes. The peel is used fresh or dried as a spice or zest for baking and drinks. Fresh tangerine juice and frozen juice concentrate are commonly available in the United States.'
voice = "en_us_006"

# arguments:
#   - input text
#   - vocie which is used for the audio
#   - output file name
#   - play sound after generating the audio
tts(text, voice, "output.mp3", play_sound=True)
