"""Check the generated portfolio, independent of the Jekyll source markup."""

import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = []
        self.refs = []
        self.images = []
        self.headings = 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "h1":
            self.headings += 1
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "img":
            self.images.append(attrs)
        for key in ("href", "src"):
            if key in attrs:
                self.refs.append(attrs[key])


root = Path(sys.argv[1]).resolve()
names = [
    "index", "automotive_can", "stm32_freertos", "resp_ecmo_monitoring", "esab",
    "embedded_real_time_systems", "glove", "postpartum_health",
]
pages = {}
errors = []
for name in names:
    path = root / (name + ".html")
    if not path.is_file():
        errors.append(f"Missing generated page: {path.name}")
        continue
    text = path.read_text(encoding="utf-8")
    if "{{" in text or "{%" in text:
        errors.append(f"Unresolved Liquid template in {path.name}")
    pages[path] = Page(text)

references = 0
for path, page in pages.items():
    if page.headings != 1:
        errors.append(f"{path.name}: expected one H1, found {page.headings}")
    if any(count > 1 for count in Counter(page.ids).values()):
        errors.append(f"{path.name}: duplicate HTML IDs")
    if any("alt" not in image for image in page.images):
        errors.append(f"{path.name}: image without alternative text")
    for reference in page.refs:
        parsed = urlsplit(reference)
        if parsed.scheme or parsed.netloc:
            continue
        references += 1
        relative = unquote(parsed.path)
        if relative.startswith("/Portfolio/"):
            target = root / relative.removeprefix("/Portfolio/")
        elif relative.startswith("/"):
            target = root / relative.lstrip("/")
        else:
            target = path.parent / relative if relative else path
        target = target.resolve()
        if target.is_dir():
            target /= "index.html"
        if not target.is_file():
            errors.append(f"{path.name}: missing target {reference}")
        elif parsed.fragment and target in pages:
            if unquote(parsed.fragment) not in pages[target].ids:
                errors.append(f"{path.name}: missing anchor {reference}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"Validated {len(pages)} production pages and {references} local references.")
