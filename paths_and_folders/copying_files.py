from pathlib import Path
import shutil

src = Path('.').resolve().parent / 'plaintext-files' / 'dad_jokes.txt'
dest = Path.home() / 'documents' / 'python_automation' / 'copying_stuff'
dest_file_path = dest / 'dad_jokes.txt'
if not src.exists():
    print('The source file does not exist')
elif dest_file_path.exists():
    print('The file already exists in the destination folder')
else:
    # note: it will silently overwrite the existing file
    shutil.copy(src, dest)