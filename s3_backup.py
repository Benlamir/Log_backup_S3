import logging, boto3
import boto3.session
from pathlib import Path

# --- Configuration du journal (Logging) ---
logging.basicConfig(
    level=logging.INFO, # On affiche les infos et les erreurs
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
#--- class that scan the files in the log directory, compare it to a register and upload the new logs to s3
class S3BackupManager:
    def __init__(self, profile_name, bucket_name, log_directory, register):
        session = boto3.Session(profile_name=profile_name)
        s3_client = session.client('s3')
        self.profile_name = profile_name
        self.bucket_name = bucket_name
        self.s3 = s3_client
        self.session = session
        self.log_directory = Path.cwd() / log_directory
        self.register = Path.cwd() / register
        if not Path(self.register).exists():
            logging.info(f"Création du registre manquant à : {self.register}")
            Path(self.register).touch()
        else:
            logging.info(f"Registre trouvé à : {self.register}")
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

if __name__ == '__main__':
    my_buckup = S3BackupManager(
            profile_name="s3-backup-bot",
            bucket_name="benlamir-logs-backup-2026",
            log_directory="logs",
            register="register.txt")
    my_buckup.upload_file()
