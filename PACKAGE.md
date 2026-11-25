# zip 안에 들어 있는 것 — 1.5.4

배포 zip에 든 고지·라이선스·사용법 파일을 **원문 그대로** 옮겼습니다(요약 없음). 프로그램 코드(`app/`)와 Python 실행부(`python/`)의 코드 파일은 싣지 않았고, 그 안의 라이선스 파일은 모두 실었습니다.

- Windows: `narration-check-1.5.4-win-x64.zip` · SHA-256 `631bd71d497be0383824efdbf880ad82ae610b55831367e97fbde663dbe8a5ad`
- Mac: `narration-check-1.5.4-mac-arm64.zip` · SHA-256 `c987b224d41079c13716b3c84463379969d486cccf1626227105bb97a5f33153`

## 1. 폴더 구성

**Windows** (`오독체크/`)

| 항목 | 파일 수 | 크기 |
|---|---|---|
| `app/` | 24 | 0.3 MB |
| `licenses/` | 3 | 46.5 KB |
| `python/` | 2643 | 294.0 MB |
| `라이선스 안내.txt` | 1 | 4.3 KB |
| `사용법.pdf` | 1 | 0.2 MB |
| `오독체크 시작.exe` | 1 | 17.0 KB |

**Mac** (`오독체크/`)

| 항목 | 파일 수 | 크기 |
|---|---|---|
| `app/` | 23 | 0.3 MB |
| `licenses/` | 3 | 29.8 KB |
| `python/` | 2401 | 275.5 MB |
| `라이선스 안내.txt` | 1 | 4.2 KB |
| `사용법.pdf` | 1 | 0.2 MB |
| `오독체크 시작.command` | 1 | 2.0 KB |

처음 실행하면 폴더 안에 `models/`(음성 인식 모델)와 `data/`(검사 결과·기록)가 새로 생깁니다. zip에는 들어 있지 않습니다.

## 2. 라이선스 안내.txt — Windows (원문 전체)

```text
나레이션 오독 체크 1.5.4 (데모 버전) · 이용 조건과 라이선스 안내

[이용 조건]
  - 나레이션 오독 체크는 개인·업무용으로 무료로 쓸 수 있습니다. 저작권은 제작자에게 있습니다.
  - 공식 배포처 밖에서 다시 배포하거나, 고쳐서 배포하거나, 판매하지 마세요.
    공식 배포처: https://github.com/richer1play/narration-check/releases/latest
  - 결과는 음성 인식에 기반한 참고용이며 정확성을 보장하지 않습니다.
    법이 허용하는 범위에서, 이 프로그램을 써서 생긴 손해에 대해 책임지지 않습니다.
  - 이후 버전이나 추가 기능은 유료로 제공될 수 있습니다. 이미 받은 버전은 계속 무료로 쓸 수 있습니다.
  - 오류 문의: richer1play@gmail.com

[OpenAI Whisper] 음성 인식의 특징 계산과 디코딩은 OpenAI Whisper의 방식을 따라 이 프로그램에서 다시 구현했습니다.
  MIT License, Copyright (c) 2022 OpenAI (전문: licenses/Whisper-MIT.txt)

이 프로그램은 아래 공개 소프트웨어를 함께 담고 있으며, 각 소프트웨어는 저마다의 라이선스를 따릅니다.
라이선스 전문은 licenses 폴더, python/LICENSE.txt, 그리고 python 폴더 안 각 패키지의 *.dist-info 폴더에 있습니다.

[FFmpeg] 오디오를 읽고 재생용 파일을 만드는 데 씁니다.
  FFmpeg 9.0.2 (gyan.dev essentials 빌드, Windows x64), GNU GPL v3 (전문: licenses/GPL-3.0.txt)
  python/Lib/site-packages/imageio_ffmpeg/binaries/ffmpeg-win-x86_64-v9.0.2.exe 에 들어 있으며, 이 프로그램은 FFmpeg를 따로 실행할 뿐 고치거나 합치지 않았습니다.
  FFmpeg 소스 코드: https://ffmpeg.org/releases/ffmpeg-9.0.2.tar.xz
  이 빌드를 만든 곳(함께 든 라이브러리 안내): https://www.gyan.dev/ffmpeg/builds/ (같은 빌드: https://github.com/GyanD/codexffmpeg/releases/tag/9.0.2)

[Python] CPython 3.12.16 (python-build-standalone), Python Software Foundation License (전문: python/LICENSE.txt)
  Python에 함께 든 OpenSSL(Apache License 2.0, 전문: licenses/Apache-2.0.txt), SQLite, zlib, libffi, bzip2, xz 등은
  각자의 라이선스를 따릅니다.

[Python 패키지] (전문: python 폴더 안 각 패키지의 *.dist-info 폴더)
  - annotated-doc 0.0.6: MIT
  - annotated-types 0.8.0: MIT
  - anyio 4.16.0: MIT
  - certifi 2026.10.23: MPL-2.0
  - charset-normalizer 3.5.2: MIT
  - click 8.5.1: BSD-3-Clause
  - colorama 0.4.6: BSD License
  - fastapi 0.163.0: MIT
  - flatbuffers 25.12.19: Apache 2.0
  - h11 0.16.0: MIT
  - idna 3.20: BSD-3-Clause
  - imageio-ffmpeg 0.8.1: BSD-2-Clause
  - kaldi_native_fbank 1.23.1: Apache-2.0
  - ml_dtypes 0.6.0: Apache-2.0
  - numpy 2.5.4: BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0
  - onnx 1.23.2: Apache-2.0
  - onnxruntime 1.32.0: MIT License
  - opentelemetry-api 1.45.2: Apache-2.0
  - packaging 26.3: Apache-2.0 OR BSD-2-Clause
  - protobuf 7.36.2: 3-Clause BSD License
  - pydantic 2.14.3: MIT
  - pydantic_core 2.50.4: MIT
  - python-multipart 0.0.33: Apache-2.0
  - RapidFuzz 3.14.6: MIT
  - regex 2026.11.9: Apache-2.0 AND CNRI-Python
  - requests 2.34.2: Apache-2.0
  - sentencepiece 0.2.3: Apache-2.0
  - sherpa_onnx 2.0.1: Apache licensed, as found in the LICENSE file
  - sherpa-onnx-core 2.0.1: Apache-2.0
  - starlette 1.10.0: BSD-3-Clause
  - tiktoken 0.14.0: MIT License
  - typing_extensions 4.16.0: PSF-2.0
  - typing-inspection 0.4.5: MIT
  - urllib3 2.8.0: MIT
  - uvicorn 0.54.0: BSD-3-Clause

[처음 실행할 때 내려받는 음성 인식 모델] (프로그램에 들어 있지 않고, 처음 실행할 때 받습니다)
  - Whisper large-v3 / large-v3-turbo (OpenAI): MIT License (전문: licenses/Whisper-MIT.txt), k2-fsa/sherpa-onnx 변환본
  - Silero VAD: MIT License, Copyright (c) 2020-present Silero Team
    위 두 모델은 k2-fsa/sherpa-onnx의 공개 저장소에서 받고, 받지 못하면 공식 배포처의 예비 사본에서 받습니다.
  - 한국어 Zipformer (k2-fsa/sherpa-onnx 공개 모델, KsponSpeech 데이터로 학습한 모델을 변환한 것)
    배포처에 라이선스가 명시되어 있지 않습니다. k2-fsa/sherpa-onnx의 공개 저장소에서만 받으며,
    받지 못하면 이 모델 없이 Whisper만으로 검사합니다.
```

## 3. 라이선스 안내.txt — Mac (원문 전체)

```text
나레이션 오독 체크 1.5.4 (데모 버전) · 이용 조건과 라이선스 안내

[이용 조건]
  - 나레이션 오독 체크는 개인·업무용으로 무료로 쓸 수 있습니다. 저작권은 제작자에게 있습니다.
  - 공식 배포처 밖에서 다시 배포하거나, 고쳐서 배포하거나, 판매하지 마세요.
    공식 배포처: https://github.com/richer1play/narration-check/releases/latest
  - 결과는 음성 인식에 기반한 참고용이며 정확성을 보장하지 않습니다.
    법이 허용하는 범위에서, 이 프로그램을 써서 생긴 손해에 대해 책임지지 않습니다.
  - 이후 버전이나 추가 기능은 유료로 제공될 수 있습니다. 이미 받은 버전은 계속 무료로 쓸 수 있습니다.
  - 오류 문의: richer1play@gmail.com

[OpenAI Whisper] 음성 인식의 특징 계산과 디코딩은 OpenAI Whisper의 방식을 따라 이 프로그램에서 다시 구현했습니다.
  MIT License, Copyright (c) 2022 OpenAI (전문: licenses/Whisper-MIT.txt)

이 프로그램은 아래 공개 소프트웨어를 함께 담고 있으며, 각 소프트웨어는 저마다의 라이선스를 따릅니다.
라이선스 전문은 licenses 폴더, python/lib/python3.12/LICENSE.txt, 그리고 python 폴더 안 각 패키지의 *.dist-info 폴더에 있습니다.

[FFmpeg] 오디오를 읽고 재생용 파일을 만드는 데 씁니다.
  FFmpeg 9.0 (osxexperts.net 빌드, macOS Apple Silicon), GNU GPL v2 이상 (전문: licenses/GPL-2.0.txt)
  python/lib/python3.12/site-packages/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v9.0 에 들어 있으며, 이 프로그램은 FFmpeg를 따로 실행할 뿐 고치거나 합치지 않았습니다.
  FFmpeg 소스 코드: https://ffmpeg.org/releases/ffmpeg-9.0.tar.xz
  이 빌드를 만든 곳(함께 든 라이브러리 안내): https://www.osxexperts.net

[Python] CPython 3.12.16 (python-build-standalone), Python Software Foundation License (전문: python/lib/python3.12/LICENSE.txt)
  Python에 함께 든 OpenSSL(Apache License 2.0, 전문: licenses/Apache-2.0.txt), SQLite, zlib, libffi, bzip2, xz 등은
  각자의 라이선스를 따릅니다.

[Python 패키지] (전문: python 폴더 안 각 패키지의 *.dist-info 폴더)
  - annotated-doc 0.0.6: MIT
  - annotated-types 0.8.0: MIT
  - anyio 4.16.0: MIT
  - certifi 2026.10.23: MPL-2.0
  - charset-normalizer 3.5.2: MIT
  - click 8.5.1: BSD-3-Clause
  - fastapi 0.163.0: MIT
  - flatbuffers 25.12.19: Apache 2.0
  - h11 0.16.0: MIT
  - idna 3.20: BSD-3-Clause
  - imageio-ffmpeg 0.8.1: BSD-2-Clause
  - kaldi_native_fbank 1.23.1: Apache-2.0
  - ml_dtypes 0.6.0: Apache-2.0
  - numpy 2.5.4: BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0
  - onnx 1.23.2: Apache-2.0
  - onnxruntime 1.23.2: MIT License
  - opentelemetry-api 1.45.2: Apache-2.0
  - packaging 26.3: Apache-2.0 OR BSD-2-Clause
  - protobuf 7.36.2: 3-Clause BSD License
  - pydantic 2.14.3: MIT
  - pydantic_core 2.50.4: MIT
  - python-multipart 0.0.33: Apache-2.0
  - RapidFuzz 3.14.6: MIT
  - regex 2026.11.9: Apache-2.0 AND CNRI-Python
  - requests 2.34.2: Apache-2.0
  - sentencepiece 0.2.3: Apache-2.0
  - sherpa_onnx 2.0.1: Apache licensed, as found in the LICENSE file
  - sherpa-onnx-core 2.0.1: Apache-2.0
  - starlette 1.10.0: BSD-3-Clause
  - tiktoken 0.14.0: MIT License
  - typing_extensions 4.16.0: PSF-2.0
  - typing-inspection 0.4.5: MIT
  - urllib3 2.8.0: MIT
  - uvicorn 0.54.0: BSD-3-Clause

[처음 실행할 때 내려받는 음성 인식 모델] (프로그램에 들어 있지 않고, 처음 실행할 때 받습니다)
  - Whisper large-v3 / large-v3-turbo (OpenAI): MIT License (전문: licenses/Whisper-MIT.txt), k2-fsa/sherpa-onnx 변환본
  - Silero VAD: MIT License, Copyright (c) 2020-present Silero Team
    위 두 모델은 k2-fsa/sherpa-onnx의 공개 저장소에서 받고, 받지 못하면 공식 배포처의 예비 사본에서 받습니다.
  - 한국어 Zipformer (k2-fsa/sherpa-onnx 공개 모델, KsponSpeech 데이터로 학습한 모델을 변환한 것)
    배포처에 라이선스가 명시되어 있지 않습니다. k2-fsa/sherpa-onnx의 공개 저장소에서만 받으며,
    받지 못하면 이 모델 없이 Whisper만으로 검사합니다.
```

## 4. 사용법.pdf (원문)

- Windows: [보기](docs/package/windows/%EC%82%AC%EC%9A%A9%EB%B2%95.pdf)
- Mac: [보기](docs/package/mac/%EC%82%AC%EC%9A%A9%EB%B2%95.pdf)

## 5. Mac 시작 파일 `오독체크 시작.command` (원문 전체)

Windows의 `오독체크 시작.exe`는 실행 파일(이진)이라 원문을 싣지 않았습니다. 하는 일은 같습니다.

```bash
#!/bin/bash
# 나레이션 오독 체크 (macOS)
# 처음 한 번: 맥이 인터넷에서 받은 이 파일을 막으면, 사용법.pdf의 [맥에서 처음 열기]대로
# 터미널에서 한 줄을 실행하세요. 그다음부터는 이 파일을 더블클릭하면 됩니다.
cd "$(dirname "$0")" || { echo "이 폴더를 열 수 없습니다."; exit 1; }
HERE="$PWD"
fail() {
  echo
  echo "$1"
  echo
  echo "자세한 방법은 사용법.pdf의 [문제가 생겼을 때]에 있습니다."
  echo "해결되지 않으면 이 창의 내용을 캡처해 이메일로 보내 주세요: richer1play@gmail.com"
  exit 1
}
if ! ls "$HERE" >/dev/null 2>&1; then
  fail "터미널이 이 폴더($HERE)를 읽지 못합니다. 오독체크 폴더를 홈 폴더(집 모양)로 옮긴 뒤 다시 실행하거나,
[시스템 설정] → [개인정보 보호 및 보안] → [파일 및 폴더] → [터미널]에서 이 폴더가 있는 곳을 허용하세요."
fi
if [ "$(uname)" = "Darwin" ]; then
  # 인터넷에서 받은 파일에 붙는 격리 표시를 지워야 함께 든 프로그램이 실행됩니다
  xattr -dr com.apple.quarantine "$HERE" 2>/dev/null
fi
PY="$HERE/python/bin/python3.12"
[ -f "$PY" ] && [ -f "$HERE/app/web_app.py" ] || fail "프로그램 파일이 없습니다. zip 파일의 압축을 다시 풀어 주세요."
[ -x "$PY" ] || chmod +x "$PY" 2>/dev/null
unset PYTHONHOME PYTHONPATH PYTHONSTARTUP
export PYTHONNOUSERSITE=1 NCHECK_MODELS="$HERE/models" NCHECK_DATA="$HERE/data"
"$PY" "$HERE/app/web_app.py" --open-browser "$@"
code=$?
if [ $code -ne 0 ] && [ $code -ne 130 ]; then
  if [ $code -eq 137 ] || [ $code -eq 126 ]; then
    fail "맥이 함께 든 프로그램(Python)을 실행하지 못하게 했습니다(코드 $code). zip 파일의 압축을 다시 푼 뒤, 사용법.pdf [맥에서 처음 열기]의 한 줄을 터미널에서 실행해 주세요."
  fi
  fail "프로그램이 오류로 끝났습니다(코드 $code). 위의 내용을 확인해 주세요."
fi
echo
echo "프로그램이 끝났습니다. 이 창을 닫으세요."
```

## 6. 라이선스·고지 파일 전체 (클릭하면 원문 전체가 열립니다)

| zip 안의 위치 | Windows | Mac |
|---|---|---|
| `licenses/Apache-2.0.txt` | [보기](docs/package/windows/licenses/Apache-2.0.txt) | [보기](docs/package/mac/licenses/Apache-2.0.txt) |
| `licenses/GPL-2.0.txt` | — | [보기](docs/package/mac/licenses/GPL-2.0.txt) |
| `licenses/GPL-3.0.txt` | [보기](docs/package/windows/licenses/GPL-3.0.txt) | — |
| `licenses/Whisper-MIT.txt` | [보기](docs/package/windows/licenses/Whisper-MIT.txt) | [보기](docs/package/mac/licenses/Whisper-MIT.txt) |
| `python/…/LICENSE.txt` | [보기](docs/package/windows/python/LICENSE.txt) | [보기](docs/package/mac/python/lib/python3.12/LICENSE.txt) |
| `python/…/site-packages/annotated_doc-0.0.6.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/annotated_doc-0.0.6.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/annotated_doc-0.0.6.dist-info/licenses/LICENSE) |
| `python/…/site-packages/annotated_types-0.8.0.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/annotated_types-0.8.0.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/annotated_types-0.8.0.dist-info/licenses/LICENSE) |
| `python/…/site-packages/anyio-4.16.0.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/anyio-4.16.0.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/anyio-4.16.0.dist-info/licenses/LICENSE) |
| `python/…/site-packages/certifi-2026.10.23.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/certifi-2026.10.23.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/certifi-2026.10.23.dist-info/licenses/LICENSE) |
| `python/…/site-packages/charset_normalizer-3.5.2.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/charset_normalizer-3.5.2.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/charset_normalizer-3.5.2.dist-info/licenses/LICENSE) |
| `python/…/site-packages/click-8.5.1.dist-info/licenses/LICENSE.txt` | [보기](docs/package/windows/python/Lib/site-packages/click-8.5.1.dist-info/licenses/LICENSE.txt) | [보기](docs/package/mac/python/lib/python3.12/site-packages/click-8.5.1.dist-info/licenses/LICENSE.txt) |
| `python/…/site-packages/colorama-0.4.6.dist-info/licenses/LICENSE.txt` | [보기](docs/package/windows/python/Lib/site-packages/colorama-0.4.6.dist-info/licenses/LICENSE.txt) | — |
| `python/…/site-packages/fastapi-0.163.0.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/fastapi-0.163.0.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/fastapi-0.163.0.dist-info/licenses/LICENSE) |
| `python/…/site-packages/h11-0.16.0.dist-info/licenses/LICENSE.txt` | [보기](docs/package/windows/python/Lib/site-packages/h11-0.16.0.dist-info/licenses/LICENSE.txt) | [보기](docs/package/mac/python/lib/python3.12/site-packages/h11-0.16.0.dist-info/licenses/LICENSE.txt) |
| `python/…/site-packages/idna-3.20.dist-info/licenses/LICENSE.md` | [보기](docs/package/windows/python/Lib/site-packages/idna-3.20.dist-info/licenses/LICENSE.md) | [보기](docs/package/mac/python/lib/python3.12/site-packages/idna-3.20.dist-info/licenses/LICENSE.md) |
| `python/…/site-packages/imageio_ffmpeg-0.8.1.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/imageio_ffmpeg-0.8.1.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/imageio_ffmpeg-0.8.1.dist-info/licenses/LICENSE) |
| `python/…/site-packages/kaldi_native_fbank-1.23.1.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/kaldi_native_fbank-1.23.1.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/kaldi_native_fbank-1.23.1.dist-info/licenses/LICENSE) |
| `python/…/site-packages/ml_dtypes-0.6.0.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/ml_dtypes-0.6.0.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/ml_dtypes-0.6.0.dist-info/licenses/LICENSE) |
| `python/…/site-packages/ml_dtypes-0.6.0.dist-info/licenses/LICENSE.eigen` | [보기](docs/package/windows/python/Lib/site-packages/ml_dtypes-0.6.0.dist-info/licenses/LICENSE.eigen) | [보기](docs/package/mac/python/lib/python3.12/site-packages/ml_dtypes-0.6.0.dist-info/licenses/LICENSE.eigen) |
| `python/…/site-packages/numpy-2.5.4.dist-info/licenses/LICENSE.txt` | [보기](docs/package/windows/python/Lib/site-packages/numpy-2.5.4.dist-info/licenses/LICENSE.txt) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/LICENSE.txt) |
| `python/…/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/include/numpy/libdivide/LICENSE.txt` | [보기](docs/package/windows/python/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/include/numpy/libdivide/LICENSE.txt) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/include/numpy/libdivide/LICENSE.txt) |
| `python/…/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/src/common/pythoncapi-compat/COPYING` | [보기](docs/package/windows/python/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/src/common/pythoncapi-compat/COPYING) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/src/common/pythoncapi-compat/COPYING) |
| `python/…/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/src/highway/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/src/highway/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/src/highway/LICENSE) |
| `python/…/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/src/multiarray/dragon4_LICENSE.txt` | [보기](docs/package/windows/python/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/src/multiarray/dragon4_LICENSE.txt) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/src/multiarray/dragon4_LICENSE.txt) |
| `python/…/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/src/npysort/x86-simd-sort/LICENSE.md` | [보기](docs/package/windows/python/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/src/npysort/x86-simd-sort/LICENSE.md) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/src/npysort/x86-simd-sort/LICENSE.md) |
| `python/…/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/src/umath/svml/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/src/umath/svml/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/src/umath/svml/LICENSE) |
| `python/…/site-packages/numpy-2.5.4.dist-info/licenses/numpy/fft/pocketfft/LICENSE.md` | [보기](docs/package/windows/python/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/fft/pocketfft/LICENSE.md) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/numpy/fft/pocketfft/LICENSE.md) |
| `python/…/site-packages/numpy-2.5.4.dist-info/licenses/numpy/linalg/lapack_lite/LICENSE.txt` | [보기](docs/package/windows/python/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/linalg/lapack_lite/LICENSE.txt) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/numpy/linalg/lapack_lite/LICENSE.txt) |
| `python/…/site-packages/numpy-2.5.4.dist-info/licenses/numpy/ma/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/ma/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/numpy/ma/LICENSE) |
| `python/…/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/LICENSE.md` | [보기](docs/package/windows/python/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/LICENSE.md) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/LICENSE.md) |
| `python/…/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/distributions/LICENSE.md` | [보기](docs/package/windows/python/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/distributions/LICENSE.md) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/distributions/LICENSE.md) |
| `python/…/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/mt19937/LICENSE.md` | [보기](docs/package/windows/python/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/mt19937/LICENSE.md) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/mt19937/LICENSE.md) |
| `python/…/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/pcg64/LICENSE.md` | [보기](docs/package/windows/python/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/pcg64/LICENSE.md) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/pcg64/LICENSE.md) |
| `python/…/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/philox/LICENSE.md` | [보기](docs/package/windows/python/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/philox/LICENSE.md) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/philox/LICENSE.md) |
| `python/…/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/sfc64/LICENSE.md` | [보기](docs/package/windows/python/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/sfc64/LICENSE.md) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/sfc64/LICENSE.md) |
| `python/…/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/splitmix64/LICENSE.md` | [보기](docs/package/windows/python/Lib/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/splitmix64/LICENSE.md) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/numpy/random/src/splitmix64/LICENSE.md) |
| `python/…/site-packages/numpy/_core/include/numpy/random/LICENSE.txt` | [보기](docs/package/windows/python/Lib/site-packages/numpy/_core/include/numpy/random/LICENSE.txt) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy/_core/include/numpy/random/LICENSE.txt) |
| `python/…/site-packages/numpy/ma/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/numpy/ma/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy/ma/LICENSE) |
| `python/…/site-packages/numpy/random/LICENSE.md` | [보기](docs/package/windows/python/Lib/site-packages/numpy/random/LICENSE.md) | [보기](docs/package/mac/python/lib/python3.12/site-packages/numpy/random/LICENSE.md) |
| `python/…/site-packages/onnx-1.23.2.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/onnx-1.23.2.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/onnx-1.23.2.dist-info/licenses/LICENSE) |
| `python/…/site-packages/onnx-1.23.2.dist-info/licenses/NOTICE` | [보기](docs/package/windows/python/Lib/site-packages/onnx-1.23.2.dist-info/licenses/NOTICE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/onnx-1.23.2.dist-info/licenses/NOTICE) |
| `python/…/site-packages/onnxruntime/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/onnxruntime/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/onnxruntime/LICENSE) |
| `python/…/site-packages/onnxruntime/ThirdPartyNotices.txt` | [보기](docs/package/windows/python/Lib/site-packages/onnxruntime/ThirdPartyNotices.txt) | [보기](docs/package/mac/python/lib/python3.12/site-packages/onnxruntime/ThirdPartyNotices.txt) |
| `python/…/site-packages/opentelemetry_api-1.45.2.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/opentelemetry_api-1.45.2.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/opentelemetry_api-1.45.2.dist-info/licenses/LICENSE) |
| `python/…/site-packages/packaging-26.3.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/packaging-26.3.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/packaging-26.3.dist-info/licenses/LICENSE) |
| `python/…/site-packages/packaging-26.3.dist-info/licenses/LICENSE.APACHE` | [보기](docs/package/windows/python/Lib/site-packages/packaging-26.3.dist-info/licenses/LICENSE.APACHE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/packaging-26.3.dist-info/licenses/LICENSE.APACHE) |
| `python/…/site-packages/packaging-26.3.dist-info/licenses/LICENSE.BSD` | [보기](docs/package/windows/python/Lib/site-packages/packaging-26.3.dist-info/licenses/LICENSE.BSD) | [보기](docs/package/mac/python/lib/python3.12/site-packages/packaging-26.3.dist-info/licenses/LICENSE.BSD) |
| `python/…/site-packages/protobuf-7.36.2.dist-info/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/protobuf-7.36.2.dist-info/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/protobuf-7.36.2.dist-info/LICENSE) |
| `python/…/site-packages/pydantic-2.14.3.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/pydantic-2.14.3.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/pydantic-2.14.3.dist-info/licenses/LICENSE) |
| `python/…/site-packages/pydantic_core-2.50.4.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/pydantic_core-2.50.4.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/pydantic_core-2.50.4.dist-info/licenses/LICENSE) |
| `python/…/site-packages/python_multipart-0.0.33.dist-info/licenses/LICENSE.txt` | [보기](docs/package/windows/python/Lib/site-packages/python_multipart-0.0.33.dist-info/licenses/LICENSE.txt) | [보기](docs/package/mac/python/lib/python3.12/site-packages/python_multipart-0.0.33.dist-info/licenses/LICENSE.txt) |
| `python/…/site-packages/rapidfuzz-3.14.6.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/rapidfuzz-3.14.6.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/rapidfuzz-3.14.6.dist-info/licenses/LICENSE) |
| `python/…/site-packages/regex-2026.11.9.dist-info/licenses/LICENSE.txt` | [보기](docs/package/windows/python/Lib/site-packages/regex-2026.11.9.dist-info/licenses/LICENSE.txt) | [보기](docs/package/mac/python/lib/python3.12/site-packages/regex-2026.11.9.dist-info/licenses/LICENSE.txt) |
| `python/…/site-packages/requests-2.34.2.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/requests-2.34.2.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/requests-2.34.2.dist-info/licenses/LICENSE) |
| `python/…/site-packages/requests-2.34.2.dist-info/licenses/NOTICE` | [보기](docs/package/windows/python/Lib/site-packages/requests-2.34.2.dist-info/licenses/NOTICE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/requests-2.34.2.dist-info/licenses/NOTICE) |
| `python/…/site-packages/sherpa_onnx-2.0.1.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/sherpa_onnx-2.0.1.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/sherpa_onnx-2.0.1.dist-info/licenses/LICENSE) |
| `python/…/site-packages/starlette-1.10.0.dist-info/licenses/LICENSE.md` | [보기](docs/package/windows/python/Lib/site-packages/starlette-1.10.0.dist-info/licenses/LICENSE.md) | [보기](docs/package/mac/python/lib/python3.12/site-packages/starlette-1.10.0.dist-info/licenses/LICENSE.md) |
| `python/…/site-packages/tiktoken-0.14.0.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/tiktoken-0.14.0.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/tiktoken-0.14.0.dist-info/licenses/LICENSE) |
| `python/…/site-packages/typing_extensions-4.16.0.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/typing_extensions-4.16.0.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/typing_extensions-4.16.0.dist-info/licenses/LICENSE) |
| `python/…/site-packages/typing_inspection-0.4.5.dist-info/licenses/LICENSE` | [보기](docs/package/windows/python/Lib/site-packages/typing_inspection-0.4.5.dist-info/licenses/LICENSE) | [보기](docs/package/mac/python/lib/python3.12/site-packages/typing_inspection-0.4.5.dist-info/licenses/LICENSE) |
| `python/…/site-packages/urllib3-2.8.0.dist-info/licenses/LICENSE.txt` | [보기](docs/package/windows/python/Lib/site-packages/urllib3-2.8.0.dist-info/licenses/LICENSE.txt) | [보기](docs/package/mac/python/lib/python3.12/site-packages/urllib3-2.8.0.dist-info/licenses/LICENSE.txt) |
| `python/…/site-packages/uvicorn-0.54.0.dist-info/licenses/LICENSE.md` | [보기](docs/package/windows/python/Lib/site-packages/uvicorn-0.54.0.dist-info/licenses/LICENSE.md) | [보기](docs/package/mac/python/lib/python3.12/site-packages/uvicorn-0.54.0.dist-info/licenses/LICENSE.md) |
