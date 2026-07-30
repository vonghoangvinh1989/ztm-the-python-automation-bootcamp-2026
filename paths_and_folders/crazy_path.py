from pathlib import Path

crazy_path = Path.home() / 'I' / 'dont' / 'exits.csv'
print(crazy_path)


if crazy_path.exists():
    with open(crazy_path, 'r') as file:
        print(file.read())
else:
    print('The file does not exist')

# note: exists use to check the path exists or not (file or folder)