from pydub import AudioSegment
import yaml
import wave
import os


def split_10sec(input_dir,output_dir):
    # Load the audio file
    audio = AudioSegment.from_wav(input_dir)

    # Split the audio into 10-second chunks
    chunks = audio[::10000]

    # Iterate through the chunks and save them
    for i, chunk in enumerate(chunks):
        chunk.export(output_dir.format(i), format="wav")

    for file in sorted(os.listdir("Output")):
        filename = os.path.join("Output", file)
        if filename.endswith(".wav"):
            with wave.open(filename) as mywav:
                duration_seconds = mywav.getnframes() / mywav.getframerate()
                left_time = 10.0 - duration_seconds
                # print(left_time)
                # print(f"Length of the WAV file: {duration_seconds:.1f} s")

                if(duration_seconds<10.0):
                    audio_val = AudioSegment.from_wav(filename)
                    # Pad the audio to 10 seconds
                    padded_audio = audio_val + AudioSegment.silent(duration=left_time)
                    # print(padded_audio)

                    # Split the audio into 10-second chunks
                    chunks_val = padded_audio[::10000]

                    # Iterate through the chunks and save them
                    for i, chunk in enumerate(chunks_val):
                        chunk.export(output_dir.format(i), format="wav")






