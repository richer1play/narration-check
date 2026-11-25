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
