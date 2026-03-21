import os
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\ffmpeg-8.1-essentials_build\bin"
import shutil
import whisper

_model = None

def _load_model():
    global _model
    if _model is None:
        _model = whisper.load_model("base")
    return _model


def _check_ffmpeg():
    if shutil.which("ffmpeg") is None:
        raise FileNotFoundError(
            "FFmpeg is required by whisper but was not found in PATH. "
            "Install FFmpeg and ensure it is available on your system PATH."
        )


def speech_to_text(audio_path: str):
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    _check_ffmpeg()
    model = _load_model()

    result = model.transcribe(audio_path)
    return result.get("text", "")

