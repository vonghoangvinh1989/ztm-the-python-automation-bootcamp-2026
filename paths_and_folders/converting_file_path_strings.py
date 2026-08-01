from pathlib import Path

# p = r'E:\LearningCourses\ZeroToMastery\ztm-the-python-automation-bootcamp\paths_and_folders'
# p = r'E:/LearningCourses/ZeroToMastery/ztm-the-python-automation-bootcamp/paths_and_folders'

# input function already convert into raw string automatically
p = input('Please enter a target folder')

path = Path(p)

if path.exists():
    print('I exist!')
