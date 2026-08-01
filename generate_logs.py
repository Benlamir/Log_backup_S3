# TODO: Importer le module 'os', random, time
import os, random, time
from pathlib import Path

# TODO: Créer une classe nommée LogGenerator (comme défini dans notre diagramme de classes)
class Log_Generator:
    # TODO: Créer la fonction d'initialisation (def __init__(self, log_directory):)
    def __init__(self, log_directory):
        # TODO: Assigner la variable 'log_directory' à 'self.log_directory'
        self.log_directory = log_directory
        # TODO: Utiliser os.path.exists() pour vérifier si le dossier self.log_directory existe déjà
        if os.path.exists(self.log_directory):
            print(f'the directory {self.log_directory} exists')
        # TODO: Si le dossier n'existe pas (if not...), utiliser os.makedirs() pour le créer
        else:
            os.makedirs(log_directory)
        # TODO: Utiliser print() pour afficher un message confirmant la création ou l'existence du dossier
            print(f'the directiry {self.log_directory} is created.')

    # TODO: Créer une fonction nommée generate_files(self, num_files):
    def generate_files(self, num_files):
        # TODO: Utiliser une boucle 'for' basique (for i in range(num_files):) pour répéter l'action
        for i in range(num_files):

            # --- DÉBUT DE LA BOUCLE ---

            # TODO: Créer une variable 'timestamp' contenant l'heure actuelle en texte (ex: "20231025_143000")
            timestamp = time.strftime("%Y%m%d_%H%M%S")

            # TODO: Créer une variable 'nom_fichier' en concaténant des chaînes de caractères (ex: "log_" + timestamp + ".txt")
            file_name = 'log_' + timestamp + '.txt'

            # TODO: Utiliser os.path.join() pour coller 'self.log_directory' et 'nom_fichier' dans une variable 'chemin_complet'
            complete_path = Path.cwd() / self.log_directory / file_name
            # TODO: Créer une liste simple de deux mots : ['SUCCESS', 'ERROR']
            outcom_log = ['SUCCESS', 'ERROR']
            # TODO: Utiliser random.choice() sur cette liste pour choisir le statut au hasard et le stocker dans une variable
            status = random.choice(outcom_log)

            # TODO: Utiliser la fonction open() avec le mode 'w' (écriture) pour ouvrir 'chemin_complet' (Chapitre 9)
            log_file = open(complete_path, 'w')   # Open the test auth.log in read mode
                # TODO: Utiliser la méthode .write() pour écrire 3 ou 4 lignes de texte dans le fichier (inclure le statut et la date)
            log_file.write('This is a test Log, created at ' + timestamp + ' with the status: ' + status + '\n')
                # TODO: Ne pas oublier d'ajouter '\n' à la fin de vos chaînes pour faire des retours à la ligne
            # TODO: Fermer le fichier (si vous n'avez pas utilisé 'with open()')
            log_file.close()

            # TODO: Utiliser print() pour annoncer que le fichier a été créé
            print(f'{file_name} is closed succesfully!')

            # TODO: Utiliser time.sleep(1) pour mettre le programme en pause 1 seconde (pour que le prochain fichier ait un timestamp différent)
            time.sleep(1)

            # --- FIN DE LA BOUCLE ---

# TODO: Écrire la condition if __name__ == '__main__':
if __name__ == '__main__':
    # TODO: Créer une variable 'mon_generateur' qui appelle LogGenerator() en lui passant le nom de votre dossier en argument (ex: "/tmp/logs")
    my_generator = Log_Generator('logs')
    # TODO: Appeler la fonction generate_files() sur 'mon_generateur' en lui demandant de faire 5 fichiers
    my_generator.generate_files(5)
