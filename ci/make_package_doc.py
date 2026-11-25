"""PACKAGE.md and docs/package/: what the release zips contain, notices and license files word for word.

    python ci/make_package_doc.py VERSION narration-check-VERSION-win-x64.zip narration-check-VERSION-mac-arm64.zip

Copies every license, notice and guide file of the two zips to docs/package/{windows,mac}/ (same paths as in
the zip) and writes PACKAGE.md: the folder layout, the full text of 라이선스 안내.txt and of the Mac launcher,
and links to every other file. Nothing is summarized.
"""
import hashlib
import os
import re
import shutil
import sys
import zipfile
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "package")
LEGAL = re.compile(r"(^|/)(LICEN[CS]E[^/]*|COPYING[^/]*|NOTICE[^/]*|ThirdPartyNotices[^/]*|AUTHORS[^/]*|COPYRIGHT[^/]*)$", re.I)


def wanted(rel: str) -> bool:
    """Files copied: the top level (except the Windows launcher program), licenses/, every license-like file."""
    if rel.endswith(".py") or rel.endswith(".exe"):
        return False
    return "/" not in rel or rel.startswith("licenses/") or bool(LEGAL.search(rel)) or "/licenses/" in rel


def text(data: bytes) -> str:
    return data.decode("utf-8-sig", "replace").replace("\r\n", "\n")


def main():
    version, zips = sys.argv[1], {"windows": sys.argv[2], "mac": sys.argv[3]}
    shutil.rmtree(OUT, ignore_errors=True)
    files, layout, sha, full = {}, {}, {}, {}
    for osname, path in zips.items():
        with open(path, "rb") as f:
            sha[osname] = hashlib.sha256(f.read()).hexdigest()
        z = zipfile.ZipFile(path)
        top = z.namelist()[0].split("/")[0]
        counts = {}
        for info in z.infolist():
            if info.filename.endswith("/"):
                continue
            rel = info.filename[len(top) + 1:]
            first = rel.split("/")[0] + ("/" if "/" in rel else "")
            n, size = counts.get(first, (0, 0))
            counts[first] = (n + 1, size + info.file_size)
            if not wanted(rel):
                continue
            dest = os.path.join(OUT, osname, *rel.split("/"))
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            data = z.read(info)
            with open(dest, "wb") as f:
                f.write(data)
            files.setdefault(rel, {})[osname] = info.file_size
            if rel in ("라이선스 안내.txt", "오독체크 시작.command"):
                full[(osname, rel)] = text(data)
        layout[osname] = (top, counts)

    def link(osname, rel):
        return f"[보기](docs/package/{osname}/{quote(rel)})"

    md = [f"# zip 안에 들어 있는 것 — {version}", "",
          "배포 zip에 든 고지·라이선스·사용법 파일을 **원문 그대로** 옮겼습니다(요약 없음). "
          "프로그램 코드(`app/`)와 Python 실행부(`python/`)의 코드 파일은 싣지 않았고, 그 안의 라이선스 파일은 모두 실었습니다.", "",
          f"- Windows: `narration-check-{version}-win-x64.zip` · SHA-256 `{sha['windows']}`",
          f"- Mac: `narration-check-{version}-mac-arm64.zip` · SHA-256 `{sha['mac']}`", "",
          "## 1. 폴더 구성", ""]
    for osname, label in (("windows", "Windows"), ("mac", "Mac")):
        top, counts = layout[osname]
        md += [f"**{label}** (`{top}/`)", "", "| 항목 | 파일 수 | 크기 |", "|---|---|---|"]
        for k in sorted(counts):
            n, size = counts[k]
            md.append(f"| `{k}` | {n} | {size / 1e6:.1f} MB |" if size >= 1e5 else f"| `{k}` | {n} | {size / 1024:.1f} KB |")
        md.append("")
    md += ["처음 실행하면 폴더 안에 `models/`(음성 인식 모델)와 `data/`(검사 결과·기록)가 새로 생깁니다. zip에는 들어 있지 않습니다.", ""]
    n = 2
    for osname, label in (("windows", "Windows"), ("mac", "Mac")):
        md += [f"## {n}. 라이선스 안내.txt — {label} (원문 전체)", "", "```text", full[(osname, "라이선스 안내.txt")].rstrip(), "```", ""]
        n += 1
    md += [f"## {n}. 사용법.pdf (원문)", "",
           f"- Windows: {link('windows', '사용법.pdf')}",
           f"- Mac: {link('mac', '사용법.pdf')}", ""]
    n += 1
    md += [f"## {n}. Mac 시작 파일 `오독체크 시작.command` (원문 전체)", "",
           "Windows의 `오독체크 시작.exe`는 실행 파일(이진)이라 원문을 싣지 않았습니다. 하는 일은 같습니다.", "",
           "```bash", full[("mac", "오독체크 시작.command")].rstrip(), "```", ""]
    n += 1
    md += [f"## {n}. 라이선스·고지 파일 전체 (클릭하면 원문 전체가 열립니다)", "",
           "| zip 안의 위치 | Windows | Mac |", "|---|---|---|"]
    skip = {"라이선스 안내.txt", "사용법.pdf", "오독체크 시작.command"}

    def key(rel):  # licenses/ first, then the Python runtime, then packages by name
        return (0 if rel.startswith("licenses/") else 1 if rel.count("/") <= 3 and "site-packages" not in rel else 2, rel.lower())
    rows = {}
    for rel, where in files.items():
        if rel in skip:
            continue
        # one row per file; the Windows and Mac paths differ only in the Python folder layout
        common = re.sub(r"^python/(Lib|lib/python3\.12)/site-packages/", "python/…/site-packages/", rel)
        common = re.sub(r"^python/(lib/python3\.12/)?LICENSE\.txt$", "python/…/LICENSE.txt", common)
        row = rows.setdefault(common, {})
        for osname in where:
            row[osname] = rel
    for common in sorted(rows, key=key):
        row = rows[common]
        cells = [link(o, row[o]) if o in row else "—" for o in ("windows", "mac")]
        md.append(f"| `{common}` | {cells[0]} | {cells[1]} |")
    md.append("")
    with open(os.path.join(ROOT, "PACKAGE.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"PACKAGE.md: {len(rows)} license files, docs/package: "
          f"{sum(len(fs) for _, _, fs in os.walk(OUT))} files")


if __name__ == "__main__":
    main()
