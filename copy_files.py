import shutil
import os
import glob
from concurrent.futures import ThreadPoolExecutor


# https://superfastpython.com/multithreaded-file-copying/
# https://pythonshowcase.com/question/how-to-perform-file-copying-in-multiple-threads-or-processor-in-python
# https://stackoverflow.com/questions/14130642/python-multi-threading-file-processing


def copy_file(src_path, dest_dir):
    dest_path = shutil.copy(src_path, dest_dir)
    print(f'copied {src_path} to {dest_path}')


def copy(src='Sensors', dest='Processed'):

    files = [y for x in os.walk('Sensors') for y in glob.glob(os.path.join(x[0], '*.csv'))]

    # On cree le pool de threads
    with ThreadPoolExecutor(10) as exe:
        _ = [exe.submit(copy_file, path, dest) for path in files]
    print('Done')



