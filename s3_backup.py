import logging, boto3, os
import boto3.session
from pathlib import Path
from dotenv import load_dotenv
# --- Configuration du journal (Logging) ---
logging.basicConfig(
    level=logging.INFO, # On affiche les infos et les erreurs
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
#--- class that scan the files in the log directory, compare it to a register and upload the new logs to s3
class S3BackupManager:
    def __init__(self, bucket_name, log_directory, register):
        load_dotenv()           # load environment variables
        access_key = os.getenv('AWS_ACCESS_KEY_ID')
        secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')


        session = boto3.Session(
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key
                )
        s3_client = session.client('s3')
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
        num_files = 0
        if not logs_to_save:
            logging.info('No files to save!')
        else:
            for file in logs_to_save:
                self.s3.upload_file(str(file), self.bucket_name, file.name)
                with open(self.register, 'a') as file_register:
                    file_register.write(file.name + '\n')
                logging.info(f'{file} [SAVED]')
                num_files += 1
            logging.info(f'{num_files} files saved!')

            

if __name__ == '__main__':
    my_buckup = S3BackupManager(
            bucket_name="benlamir-logs-backup-2026",
            log_directory="logs",
            register="register.txt")
    my_buckup.upload_file()
