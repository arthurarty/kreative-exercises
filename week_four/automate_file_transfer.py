import ftplib
import os
import shutil

import schedule
from dotenv import load_dotenv

# Assumes you have created a .env file with FTP USER details
load_dotenv()  # take environment variables from .env.


FTP_HOST = os.getenv('FTP_HOST')
FTP_PASSWORD = os.getenv('FTP_PASSWORD')
FTP_USERNAME = os.getenv('FTP_USERNAME')


def copy_remote_files(host: str, username: str, password: str, src_dir: str, dest_folder: str):
    """
    Using FTP connect to a remote server and copy the files in 'source_directory' specified
    to the destination folder on the local machine.
    """
    new_files_found = 0
    with ftplib.FTP(host=host, user=username, passwd=password) as ftp:
        status = ftp.getwelcome()
        if status == '220 Rebex FTP Server ready.':
            print('Connected successfully')
        else:
            print('Failed to connect to remove server')
            return
        ftp.cwd(src_dir)
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
            print(f"Folder '{dest_folder}' created successfully.")
        print('Copying files please wait...')
        for file_name in ftp.nlst():
            local_filepath = os.path.join(dest_folder, file_name)
            if os.path.exists(local_filepath):
                # skip files we already downloaded
                continue
            else:
                try:
                    with open(local_filepath, 'wb') as local_file:
                        ftp.retrbinary("RETR " + file_name, local_file.write)
                    new_files_found += 1
                except Exception:
                    print(f'Failed to write file to {local_filepath}')
        print(f'Done Copying Files. New files found: {new_files_found}')


def move_files_to_internal_network(src_dir: str, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        print(f"Folder '{dest_folder}' created successfully.")
    shutil.copytree(src_dir, dest_folder, dirs_exist_ok=True)
    print('Done Copying to internal network')


def main():
    """
    Connect to remote server and copy files to internal network
    """
    copy_remote_files(FTP_HOST, FTP_USERNAME, FTP_PASSWORD, 'pub/example', 'remote_files')
    move_files_to_internal_network('remote_files', 'internal_copy_folder')


# schedule email to go out at 3:00pm everyday.
schedule.every().day.at("15:00").do(main)


while True:
    schedule.run_pending()
