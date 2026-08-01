from pathlib import Path
import shutil

p = Path.home() / 'documents' / 'python_automation' / 'doomed_folder'

if p.exists():
    p.rmdir() # only remove empty folder


p2 = Path.home() / 'documents' / 'python_automation' / 'fun_with_folders'

if p2.exists():
    # p2.rmdir()
    shutil.rmtree(p2) # delete folder with anything inside, cautious here because it will remove