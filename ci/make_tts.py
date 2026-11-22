"""Makes ci/test_narration.mp3 and ci/test_script.txt: made-up sentences read by espeak-ng (a free synthetic
voice, no real person), with two planted mistakes the check has to find.

    NCHECK_SRC=<program source> python ci/make_tts.py ci
(needs espeak-ng with the Korean voice and the program source for its ffmpeg)
"""
import os
import subprocess
import sys
import wave

import numpy as np

sys.path.insert(0, os.environ.get("NCHECK_SRC", "."))
from ncheck.audio import find_ffmpeg  # noqa: E402

SCRIPT = [
    "비가 그친 오후, 지훈은 오래된 서점 문을 열었습니다.",
    "먼지 쌓인 책장 사이로 낡은 일기장 하나가 눈에 띄었죠.",
    "첫 장을 넘기자 낯익은 이름이 적혀 있었는데요.",
    "그것은 십 년 전 사라진 형의 이름이었습니다.",
    "지훈은 떨리는 손으로 다음 장을 넘겼습니다.",
    "그곳에는 형이 마지막으로 남긴 주소가 있었습니다.",
    "다음 날 아침, 지훈은 그 주소를 찾아 기차에 올랐죠.",
    "과연 그곳에서 형의 흔적을 찾을 수 있을까요?",
]
# what the voice actually reads: line 2 낡은 -> 남은 (misread), line 5 without 떨리는 (dropped word)
READ = list(SCRIPT)
READ[1] = READ[1].replace("낡은", "남은")
READ[4] = READ[4].replace("떨리는 ", "")

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
pcm = []
for i, line in enumerate(READ):
    w = os.path.join(out, f"_{i}.wav")
    subprocess.run(["espeak-ng", "-v", "ko", "-s", "140", "-w", w, line], check=True)
    with wave.open(w) as f:
        sr = f.getframerate()
        pcm.append(np.frombuffer(f.readframes(f.getnframes()), dtype="<i2"))
    pcm.append(np.zeros(int(sr * 0.8), dtype="<i2"))
    os.remove(w)
audio = np.concatenate([np.zeros(int(sr * 0.5), dtype="<i2")] + pcm)
raw = os.path.join(out, "_all.raw")
audio.tofile(raw)
subprocess.run([find_ffmpeg(), "-nostdin", "-loglevel", "error", "-y", "-f", "s16le", "-ar", str(sr), "-ac", "1", "-i", raw,
                "-ar", "16000", "-b:a", "64k", os.path.join(out, "test_narration.mp3")], check=True)
os.remove(raw)
with open(os.path.join(out, "test_script.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(SCRIPT) + "\n")
print(f"{len(audio) / sr:.1f}s at {sr} Hz ->", os.listdir(out))
