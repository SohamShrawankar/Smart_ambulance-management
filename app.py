import sounddevice as sd
import numpy as np
import queue
import threading
from faster_whisper import WhisperModel

samplerate = 16000
block_duration = 0.5 # s e c o n d s
chunk_duration = 2 # s e c o n d s
channels = 1

frames_per_block = int(samplerate * block_duration)
frames_per_chunk = int(samplerate * chunk_duration)

audio_queue = queue.Queue()
audio_buffer = []

model = WhisperModel("small.en", device="cpu", compute_type="int8")

def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    audio_queue.put(indata.copy())

def recorder():
    with sd.InputStream(samplerate=samplerate, channels=channels,
                        callback=audio_callback, blocksize=frames_per_block):
        print("🎙️ Listening... Press Ctrl+C to stop.")
        while True:
            sd.sleep(100)

def transcriber():
    global audio_buffer
    while True:
        block = audio_queue.get()
        audio_buffer.append(block)

        total_frames = sum(len(b) for b in audio_buffer)
        if total_frames >= frames_per_chunk:
            audio_data = np.concatenate(audio_buffer)[:frames_per_chunk]
            audio_buffer = [] # Clear buffer

            audio_data = audio_data.flatten().astype(np.float32)

            # Transcription without timestamps
            segments, _ = model.transcribe(
                audio_data,
                language="en",
                beam_size=1 # Max speed
            )

            for segment in segments:
                print(f"{segment.text}")

# Start threads
threading.Thread(target=recorder, daemon=True).start()
transcriber()
