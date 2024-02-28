from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr

# Load the audio file
audio_path = "/mnt/data/26 Feb 2024 at 13_00_18.mp4"
audio = AudioSegment.from_file(audio_path, format="mp4")

# Split the audio file into chunks on silence for better processing
chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=-40)

# Use the first chunk for transcription as a sample
chunk_path = "/mnt/data/audio_chunk.wav"
chunks[0].export(chunk_path, format="wav")

# Use speech recognition to transcribe the audio file
r = sr.Recognizer()
with sr.AudioFile(chunk_path) as source:
  audio_data = r.record(source)
  text = r.recognize_google(audio_data)

text

# convert file

from moviepy.editor import VideoFileClip

# Convert video to audio
video_path = "/mnt/data/26 Feb 2024 at 13_00_18.mp4"
audio_path = "/mnt/data/extracted_audio.wav"

video_clip = VideoFileClip(video_path)
audio_clip = video_clip.audio
audio_clip.write_audiofile(audio_path)
