from pathlib import Path
import shutil

# purpose: 'fun_with_folders' inside 'copying_stuff'
# note: when copying folder, need to put the name of folder we want to copy 'fun_with_folders' in dest also
# anything inside folders was copied too
src = Path.home() / 'documents' / 'python_automation' / 'fun_with_folders'
dest = Path.home() / 'documents' / 'python_automation' / 'copying_stuff' / "fun_with_folders"

shutil.copytree(src, dest, dirs_exist_ok=True)