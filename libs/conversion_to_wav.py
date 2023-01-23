from pydub import AudioSegment


## convert mpe to wav
def conver_mp3_to_wav(SRC_IMG_PATH,DST_IMG_PATH):
    sound = AudioSegment.from_mp3(SRC_IMG_PATH)
    sound.export(DST_IMG_PATH, format="wav")

