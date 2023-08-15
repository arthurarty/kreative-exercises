import ftplib
import os
import time
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
        for file_name in ftp.nlst():
            local_filepath = os.path.join(dest_folder, file_name)
            if os.path.exists(local_filepath):
                # skip files we already downloaded
                continue
            else:
                new_files_found += 1
                with open(local_filepath, 'wb') as local_file:
                    ftp.retrbinary("RETR " + file_name, local_file.write)
        print(f'New files found: {new_files_found}')


copy_remote_files(FTP_HOST, FTP_USERNAME, FTP_PASSWORD, 'pub/example', 'remote_files')
