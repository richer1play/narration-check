# zip 안에 들어 있는 것 (1.5.4 데모 버전)

받은 zip을 풀면 `오독체크` 폴더 하나가 생깁니다.

| 파일·폴더 | 내용 |
|---|---|
| `오독체크 시작.exe` (Windows)<br>`오독체크 시작.command` (Mac) | 프로그램을 여는 파일 |
| `사용법.pdf` | 2쪽 사용법 · [Windows용 보기](docs/guide-windows.pdf) · [Mac용 보기](docs/guide-mac.pdf) |
| `라이선스 안내.txt` | 이용 조건과 함께 든 공개 소프트웨어 목록 · [Windows용 보기](docs/license-notice-windows.txt) · [Mac용 보기](docs/license-notice-mac.txt) |
| `licenses/` | 라이선스 전문 3개: Whisper MIT, Apache 2.0, GPL (Windows는 v3, Mac은 v2) |
| `app/` | 프로그램 코드와 화면 (Windows에만 문제 확인용 `콘솔 창으로 시작.bat`) |
| `python/` | 함께 든 Python 3.12, 부품 35개, FFmpeg |

처음 실행하면 폴더 안에 `models/`(음성 인식 모델, 약 1.4GB)와 `data/`(검사 결과·검수 표시·기록)가 새로 생깁니다.
녹음과 대본은 컴퓨터 밖으로 보내지 않습니다.

## 이용 조건 (요약)

- 개인·업무용으로 무료로 쓸 수 있습니다. 저작권은 제작자에게 있습니다.
- 공식 배포처 밖에서 다시 배포하거나, 고쳐서 배포하거나, 판매할 수 없습니다.
- 결과는 음성 인식에 기반한 참고용이며 정확성을 보장하지 않습니다.
- 이후 버전이나 추가 기능은 유료일 수 있습니다. 이미 받은 버전은 계속 무료로 쓸 수 있습니다.
- 오류 문의: richer1play@gmail.com

## 함께 든 공개 소프트웨어 (요약)

| 이름 | 라이선스 |
|---|---|
| FFmpeg 9.0.2 (Windows) / 9.0 (Mac) | GPL v3 / GPL v2 이상 · 소스: ffmpeg.org |
| Python 3.12.16 | Python Software Foundation License |
| Python 부품 35개 (numpy, onnxruntime, sherpa-onnx, fastapi 등) | MIT, BSD, Apache 2.0 등 (부품별 목록은 라이선스 안내) |
| OpenAI Whisper의 방식을 따라 다시 구현한 부분 | MIT |
| 처음 실행 때 받는 모델: Whisper, Silero VAD | MIT |
| 처음 실행 때 받는 모델: 한국어 Zipformer | 배포처에 라이선스 명시 없음 |
