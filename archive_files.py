import shutil
import os
import glob
import datetime
from zipfile import ZipFile
from concurrent.futures import ThreadPoolExecutor


def archive_and_copy_file(src_path, dest_dir):
    filename = os.path.basename(src_path).split(".")[0] + ".zip"
    zip_path = os.path.join(dest_dir, filename)
    with ZipFile(zip_path, 'w') as zip_obj:
        zip_obj.write(src_path)
        print(f'{zip_path} archived')
    os.remove(src_path)
    print(f'{src_path} removed')
    dest_path = shutil.copy(zip_path, dest_dir)
    print(f'.copied {src_path} to {dest_path}')


def archive(src='Processed', dest='Archive'):
    if os.path.exists(src) and not os.path.isfile(src):
        # Controle du chemin
        if not os.listdir(src):
            print(f'{src} is empty')
        else:
            files = [os.path.join(src, name) for name in os.listdir(src)]

            # On cree le pool de threads
            with ThreadPoolExecutor(10) as exe:
                _ = [exe.submit(archive_and_copy_file, path, dest) for path in files]
            print('Done')
    else:
        print("Invalid path or not a directory")
