"""Build deployable static output for GitHub project Pages or a custom domain."""
import argparse
from pathlib import Path
import re
import shutil
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--base-path', default='/portfolio')
parser.add_argument('--origin', default='https://lalbuquerque.github.io')
args = parser.parse_args()
base = '/' + args.base_path.strip('/') if args.base_path.strip('/') else ''
origin = args.origin.rstrip('/')
if not re.fullmatch(r'(?:/[A-Za-z0-9._-]+)*', base):
    parser.error('Invalid base path')
subprocess.run([sys.executable, str(ROOT/'scripts/build_locales.py')], check=True)
output = ROOT/'_site'
if output.exists():
    shutil.rmtree(output)
shutil.copytree(ROOT/'dist', output)
for file in output.rglob('*.html'):
    html = file.read_text()
    html = html.replace('https://lucas-albuquerque-portfolio.focusedcatfish4.chatgpt.site', origin + base)
    html = re.sub(r'((?:href|src)=\")/(?!/)', lambda m: m[1] + base + '/', html)
    file.write_text(html)
(output/'.nojekyll').touch()
print(f'Built {origin}{base}/ in {output}')
