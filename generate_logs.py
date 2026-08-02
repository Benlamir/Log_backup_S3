import os, random, time     # importer les modules os,random, time and Path
from pathlib import Path

class Log_Generator:   # create the class
    def __init__(self, log_directory):  # 
        self.log_directory = log_directory  # assign the attribute to the argument
        if os.path.exists(self.log_directory):  # Use the os.oath.exists to check if the folder exists
            print(f'the directory {self.log_directory} exists')
        else:
            os.makedirs(log_directory)  # if the folder dont exists create it
            print(f'the directiry {self.log_directory} is created.')

    def generate_files(self, num_files): # Create the function for generating fake logs
        for i in range(num_files):  #for loop to repeate the action

            # ---lOOP_START ---

            timestamp = time.strftime("%Y%m%d_%H%M%S") #create a variable that stors the current date and time

            file_name = 'log_' + timestamp + '.txt'  # Create a file name by concatenating the chaine characters

            complete_path = Path.cwd() / self.log_directory / file_name  # storing the path to the file
            outcom_log = ['SUCCESS', 'ERROR']  # List of status
            status = random.choice(outcom_log)  # determin a random status

            log_file = open(complete_path, 'w')   # Open the file il the previously created variable with w mode
            log_file.write('This is a test Log, created at ' + timestamp + ' with the status: ' + status + '\n') # W#rite random logs using previously created file_name and timestamp
            log_file.close()  # Close the file

            print(f'{file_name} is closed succesfully!')

            time.sleep(1)  # pause for & second for the file names to be diferent

            # ---END_LOOP---

if __name__ == '__main__':
    my_generator = Log_Generator('logs')  # Create a variable that calls the class
    my_generator.generate_files(5)  # Calls the function generate_files and passing ( as argument wich create 5 fake log_file 
