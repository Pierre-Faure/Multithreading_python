import time
import copy_files
import archive_files


def main():
    print('Program start')
    time.sleep(3)
    print('Copying files')
    copy_files.copy()
    time.sleep(3)
    print('Archiving files')
    archive_files.archive()
    print('Program finished')


if __name__ == '__main__':
    main()
