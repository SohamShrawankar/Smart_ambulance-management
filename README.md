# Smart_ambulance-management

# 🎙️ Real-Time Speech-to-Text Transcriber

This project provides a **real-time speech-to-text system** using [faster-whisper](https://github.com/SYSTRAN/faster-whisper) and [sounddevice](https://python-sounddevice.readthedocs.io/).
It listens to microphone input continuously and transcribes speech into text with minimal latency.

---

## ✨ Features

* ✅ Real-time microphone streaming
* ✅ Uses **faster-whisper** (optimized Whisper ASR)
* ✅ Lightweight & fast (`small.en` model with `int8` quantization)
* ✅ Threaded recorder + transcriber
* ✅ Works **offline** after downloading model

---

## ⚡ Requirements

Make sure you have Python **3.9+** installed.
Then install dependencies:

```bash
pip install sounddevice numpy faster-whisper
```

---

## ▶️ Usage

Clone this repository and run:

```bash
python app.py
```

You will see:

```
🎙️ Listening... Press Ctrl+C to stop.
```

Start speaking, and the transcription will appear in the terminal in real-time.

---

## ⚙️ Configuration

You can tweak parameters inside `app.py`:

| Parameter        | Default  | Description                           |
| ---------------- | -------- | ------------------------------------- |
| `samplerate`     | 16000    | Audio sample rate                     |
| `block_duration` | 0.5 sec  | Size of each audio block              |
| `chunk_duration` | 2 sec    | Audio chunk before sending to Whisper |
| `channels`       | 1        | Mono audio                            |
| `model`          | small.en | Whisper model variant                 |
| `compute_type`   | int8     | Quantization for speed/low memory     |

---
