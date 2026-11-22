"""Download the package of one release of this repository (drafts too) for testing.

    python ci/fetch_release.py TAG win-x64.zip OUTDIR
Uses GITHUB_TOKEN and GITHUB_REPOSITORY, which GitHub Actions provides.
"""
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):  # the file itself is fetched without the token
        return None


def _api(url: str, accept: str = "application/vnd.github+json", follow: bool = True):
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
                                               "Accept": accept, "X-GitHub-Api-Version": "2022-11-28"})
    opener = urllib.request.build_opener() if follow else urllib.request.build_opener(_NoRedirect)
    return opener.open(req, timeout=120)


def find_release(repo: str, tag: str) -> dict:
    page = 1
    while True:
        with _api(f"https://api.github.com/repos/{repo}/releases?per_page=100&page={page}") as r:
            items = json.load(r)
        if not items:
            sys.exit(f"릴리스 {tag} 를 찾지 못했습니다.")
        for rel in items:
            if rel["tag_name"] == tag:
                return rel
        page += 1


def main():
    tag, suffix, out = sys.argv[1:4]
    rel = find_release(os.environ["GITHUB_REPOSITORY"], tag)
    asset = next((a for a in rel["assets"] if a["name"].endswith(suffix)), None)
    if not asset:
        sys.exit(f"릴리스 {tag} 에 *{suffix} 파일이 없습니다: {[a['name'] for a in rel['assets']]}")
    os.makedirs(out, exist_ok=True)
    dest = os.path.join(out, asset["name"])
    try:
        resp = _api(asset["url"], accept="application/octet-stream", follow=False)
    except urllib.error.HTTPError as e:
        if e.code not in (301, 302, 303, 307, 308):
            raise
        resp = urllib.request.urlopen(e.headers["Location"], timeout=600)
    h = hashlib.sha256()
    with resp, open(dest, "wb") as f:
        while True:
            b = resp.read(1 << 20)
            if not b:
                break
            f.write(b)
            h.update(b)
    size = os.path.getsize(dest)
    print(f"{asset['name']} ({'임시' if rel['draft'] else '공개'} 릴리스 {tag}) {size} bytes sha256 {h.hexdigest()}")
    if size != asset["size"]:
        sys.exit(f"크기가 다릅니다: {size} != {asset['size']}")


if __name__ == "__main__":
    main()
