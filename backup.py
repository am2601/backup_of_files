import os
import time
import sys
import zipfile

dir = 'C:\\'  # enter directory, where you want save backups of files or folders
def check_args(massive):
    if len(massive) > 1:
        return os.path.basename(massive[1])
    else:
        exit()

target_dir = os.path.join(dir, 'backup_folder')

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

source = check_args(sys.argv)
# print(source)
today = target_dir + os.sep + time.strftime('%d.%m.%Y')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
z = zipfile.ZipFile(today + os.sep + now + '.zip', 'w')

if os.path.isdir(source):
    for root, dirs, files in os.walk(source):
        for file in files:
            z.write(os.path.join(root, file))
else:
    z.write(source)
z.close()


