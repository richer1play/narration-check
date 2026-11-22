"""Smoke test of a running 나레이션 오독 체크 package: one real check through its web API.

    <package>/python/python3 ci/smoke.py --base auto --model turbo --out out

``--base auto`` finds the program on ports 8000-8009 (it takes the next port when 8000 is busy) and writes
the address to OUT/base.txt for the later steps.

Runs with the package's own Python (standard library only). Exit code 0 = passed.
The test narration has two planted mistakes (see make_tts.py) that the check must report.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
FAILS: list[str] = []


def ok(cond: bool, what: str) -> bool:
    print(("ok    " if cond else "FAIL  ") + what, flush=True)
    if not cond:
        FAILS.append(what)
    return cond


def get(url: str, timeout: float = 30):
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return r.status, r.headers.get("content-type", ""), r.read()


def get_json(url: str):
    return json.loads(get(url)[2])


def post(url: str, body: bytes = b"", ctype: str = "application/octet-stream"):
    req = urllib.request.Request(url, data=body, method="POST", headers={"x-ncheck": "1", "content-type": ctype})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read() or b"{}")


def multipart(fields: dict, files: dict) -> tuple[bytes, str]:
    b = uuid.uuid4().hex
    out = []
    for k, v in fields.items():
        out.append(f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
    for k, (name, data) in files.items():
        out.append(f'--{b}\r\nContent-Disposition: form-data; name="{k}"; filename="{name}"\r\n'
                   f"Content-Type: application/octet-stream\r\n\r\n".encode("utf-8") + data + b"\r\n")
    out.append(f"--{b}--\r\n".encode())
    return b"".join(out), f"multipart/form-data; boundary={b}"


def wait(what: str, fn, limit: float, every: float = 2.0, say=None):
    t0 = time.time()
    last_say = 0.0
    while time.time() - t0 < limit:
        try:
            v = fn()
            if v:
                return v
        except (urllib.error.URLError, ConnectionError, TimeoutError, OSError):
            pass
        if say and time.time() - last_say > 30:
            last_say = time.time()
            try:
                print(f"      … {say()}", flush=True)
            except Exception:
                pass
        time.sleep(every)
    raise TimeoutError(f"{what}: {limit:.0f}초 안에 끝나지 않음")


def flagged(line: dict, word: str) -> list:
    """Reported differences that cover ``word`` of the script line."""
    t = line["text"]
    a = t.index(word)
    b = a + len(word)
    return [(r["v"], r["k"], r.get("h")) for r in line["r"]
            if r["sw"][0] < b and r["sw"][1] > a and r["v"] in ("misread", "check")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="auto")
    ap.add_argument("--audio", default=os.path.join(HERE, "test_narration.mp3"))
    ap.add_argument("--script", default=os.path.join(HERE, "test_script.txt"))
    ap.add_argument("--model", default="turbo", choices=["turbo", "large-v3"])
    ap.add_argument("--version", help="expected program version (e.g. 1.5.3)")
    ap.add_argument("--out", default="out")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    t0 = time.time()

    def find():
        bases = [a.base.rstrip("/")] if a.base != "auto" else [f"http://127.0.0.1:{p}" for p in range(8000, 8010)]
        for b in bases:
            try:
                h = get_json(b + "/healthz")
            except Exception:
                continue
            if h.get("app") == "ncheck":
                return b, h
        return None

    base, health = wait("프로그램 시작", find, 180)
    with open(os.path.join(a.out, "base.txt"), "w") as f:
        f.write(base)
    ok(health.get("app") == "ncheck", f"프로그램이 응답함: {health}")
    if a.version:
        ok(health.get("version") == a.version, f"버전 {health.get('version')} (기대 {a.version})")

    def ready():
        s = get_json(base + "/api/status")
        if s.get("error"):
            raise SystemExit(f"FAIL  모델 준비 오류: {s['error']}")
        return s if s.get("models_ready") else None

    wait("음성 인식 모델 준비", ready, 1800, 5,
              say=lambda: get_json(base + "/api/status").get("message", ""))
    ok(True, f"모델 준비 완료 ({time.time() - t0:.0f}초)")

    with open(a.audio, "rb") as f:
        audio = f.read()
    with open(a.script, "rb") as f:
        script = f.read()
    body, ctype = multipart({"model": a.model}, {"audio": ("시험_나레이션.mp3", audio), "script": ("시험_대본.txt", script)})
    job = post(base + "/api/jobs", body, ctype)
    jid = job["id"]
    with open(os.path.join(a.out, "job_id.txt"), "w") as f:
        f.write(jid)
    print(f"      검사 시작: {jid} ({a.model})", flush=True)

    t1 = time.time()

    def finished():
        j = get_json(f"{base}/api/jobs/{jid}")
        return j if j.get("state") in ("done", "error", "cancelled") else None

    j = wait("검사", finished, 2400, 3, say=lambda: get_json(f"{base}/api/jobs/{jid}").get("message", ""))
    ok(j["state"] == "done", f"검사 끝남: {j['state']} {j.get('error') or ''} ({time.time() - t1:.0f}초)")

    res = get_json(f"{base}/api/jobs/{jid}/result")
    with open(os.path.join(a.out, "result.json"), "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    lines = {L["i"]: L for L in res.get("lines", [])}
    ok(len(lines) == 8, f"대본 8문장과 모두 맞춤: {len(lines)}")
    if 1 in lines:
        ok(bool(flagged(lines[1], "낡은")), f"심어 둔 오독(낡은 → 남은)을 찾음: {flagged(lines[1], '낡은')}")
    if 4 in lines:
        ok(bool(flagged(lines[4], "떨리는")), f"심어 둔 빠뜨림(떨리는)을 찾음: {flagged(lines[4], '떨리는')}")
    warns = res.get("warnings") or []
    ok(not any("보조 인식기" in w for w in warns), f"보조 인식기 정상 동작 (안내: {warns})")
    ok(os.path.exists(os.path.join(a.out, "result.json")), "결과 저장")

    code, ctype, pdf = get(base + "/guide")
    ok(code == 200 and pdf[:4] == b"%PDF", f"사용법 PDF 열림 ({ctype}, {len(pdf) // 1024} KB)")
    code, _, page = get(base + "/")
    ok(code == 200 and "오류 문의" in page.decode("utf-8", "replace"), "처음 화면과 오류 문의 이메일 표시")

    print(f"\n{'통과' if not FAILS else '실패 ' + str(len(FAILS)) + '건'} · 전체 {time.time() - t0:.0f}초", flush=True)
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
