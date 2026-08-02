import logging, boto3
import boto3.session
from pathlib import Path

#--- class that scan the files in the log directory, compare it to a register and upload the new logs to s3
class S3BackupManager:
    def __init__(self, profile_name, bucket_name, log_directory, register):
        session = boto3.Session(profile_name=profile_name)
        s3_client = session.client('s3')
        self.profile_name = profile_name
        self.bucket_name = bucket_name
        self.s3 = s3_client
        self.session = session
        self.log_directory = log_directory
        self.register = register

    #---this function read the content in the file logs, compared them to the resigter and return the non saved logs
    def scan_local_directory(self):
        with open(self.register, 'r') as file_register:
            content = file_register.read()
            register = content.splitlines()

        logs_to_save = []
        log_path = Path.cwd() / self.log_directory
        for file in log_path.iterdir():
            if file.is_file() and file.name not in register:
                logs_to_save.append(file)
        return logs_to_save

    #---take the returned list of non saved logs in the previous def and upload it to s3 then write the saved logs t #to the register
    def upload_file(self):
        logs_to_save = self.scan_local_directory()
        for file in logs_to_save:
            self.s3.upload_file(str(file), self.bucket_name, file.name)
            with open(self.register, 'a') as file_register:
                file_register.write(file.name + '\n')
