"""Check deployed HTML paths, locale routes and asset references."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
ROOT=Path(__file__).resolve().parents[1]/'_site'
BASE='/portfolio-website'
class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]
    def handle_starttag(self,tag,attrs):
        self.links.extend(v for k,v in attrs if k in ('href','src') and v)
for file in ROOT.rglob('*.html'):
    parser=Links(); parser.feed(file.read_text())
    for link in parser.links:
        url=urlparse(link)
        if url.scheme or url.netloc or not url.path: continue
        pathname=unquote(url.path)
        if pathname.startswith('/'):
            assert pathname.startswith(BASE+'/'), f'{file}: outside project path: {link}'
            target=ROOT/pathname[len(BASE)+1:]
        else:
            target=file.parent/pathname
        if target.is_dir(): target=target/'index.html'
        assert target.exists(), f'{file}: missing {link}'
    assert 'focusedcatfish' not in file.read_text()
print('GitHub Pages paths, localized pages and assets validated.')
