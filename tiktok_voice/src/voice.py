# author: Giorgio
# date: 23.08.2024
# topic: TikTok-Voice-TTS
# version: 1.3

from enum import Enum

# Enum to define available voices for text-to-speech conversion
class Voice(Enum):
    # DISNEY VOICES
    GHOSTFACE = 'en_us_ghostface'
    CHEWBACCA = 'en_us_chewbacca'
    C3PO = 'en_us_c3po'
    STITCH = 'en_us_stitch'
    STORMTROOPER = 'en_us_stormtrooper'
    ROCKET = 'en_us_rocket'
    # ENGLISH VOICES
    EN_AU_FEMALE_1 = 'en_au_001'
    EN_AU_MALE_1 = 'en_au_002'
    EN_UK_MALE_1 = 'en_uk_001'
    EN_UK_MALE_2 = 'en_uk_003'
    EN_US_FEMALE_1 = 'en_us_001'
    EN_US_FEMALE_2 = 'en_us_002'
    EN_US_MALE_1 = 'en_us_006'
    EN_US_MALE_2 = 'en_us_007'
    EN_US_MALE_3 = 'en_us_009'
    EN_US_MALE_4 = 'en_us_010'
    # EUROPE VOICES
    FR_MALE_1 = 'fr_001'
    FR_MALE_2 = 'fr_002'
    DE_FEMALE = 'de_001'
    DE_MALE = 'de_002'
    ES_MALE = 'es_002'
    # AMERICA VOICES
    ES_MX_MALE = 'es_mx_002'
    BR_FEMALE_1 = 'br_001'
    BR_FEMALE_2 = 'br_003'
    BR_FEMALE_3 = 'br_004'
    BR_MALE = 'br_005'
    # ASIA VOICES
    ID_FEMALE = 'id_001'
    JP_FEMALE_1 = 'jp_001'
    JP_FEMALE_2 = 'jp_003'
    JP_FEMALE_3 = 'jp_005'
    JP_MALE = 'jp_006'
    KR_MALE_1 = 'kr_002'
    KR_FEMALE = 'kr_003'
    KR_MALE_2 = 'kr_004'
    # SINGING VOICES
    EN_FEMALE_ALTO = 'en_female_f08_salut_damour'
    EN_MALE_TENOR = 'en_male_m03_lobby'
    EN_FEMALE_WARMY_BREEZE = 'en_female_f08_warmy_breeze'
    EN_MALE_SUNSHINE_SOON = 'en_male_m03_sunshine_soon'
    # OTHER
    EN_MALE_NARRATION = 'en_male_narration'
    EN_MALE_FUNNY = 'en_male_funny'
    EN_FEMALE_EMOTIONAL = 'en_female_emotional'

    # Function to check if a string matches any enum member name
    def from_string(input_string: str):
        # Iterate over all enum members
        for voice in Voice:
            if voice.name == input_string:
                return voice
        return None