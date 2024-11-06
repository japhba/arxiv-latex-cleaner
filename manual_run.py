import logging
from pathlib import Path
from arxiv_latex_cleaner.__main__ import PARSER
from arxiv_latex_cleaner.arxiv_latex_cleaner import run_arxiv_cleaner

repo_name = 'tex_neurips24'
path = Path.home() / ('learning-context-sensing') / repo_name
path_svg_rel = f"svg-inkscape"
ARGS = vars(PARSER.parse_args(f'--svg_inkscape {path_svg_rel} --verbose {path}'.split()))

final_args = ARGS




logging.basicConfig(level=logging.INFO)

run_arxiv_cleaner(final_args)

# Replace any line containing 'checklist' in the specified file.
import re
file_path = Path(str(path).replace(repo_name, f"{repo_name}_arXiv")) / 'main.tex'
text = re.sub(r"\\input\{.*checklist.*\}", "", file_path.read_text())
file_path.write_text(text)

exit(0)