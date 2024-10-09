import os
import time
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

# Chemin du répertoire racine où sont stockés les dossiers de date
root_folder = "/chemin/vers/ton/dossier"  # Modifie avec le chemin correct

# Fonction pour convertir une chaîne de date "DD.MM.YYYY" en timestamp
def date_string_to_timestamp(date_str):
    try:
        return time.mktime(datetime.strptime(date_str, "%d.%m.%Y").timetuple())
    except ValueError:
        print(f"Format de date invalide pour : {date_str}")
        return None

# Fonction pour mettre à jour la date de création et modification d'un fichier
def update_file_dates(file_path, timestamp):
    try:
        # Met à jour les dates de modification et d'accès du fichier
        os.utime(file_path, (timestamp, timestamp))
        print(f"Dates mises à jour pour : {file_path}")
    except Exception as e:
        print(f"Erreur lors de la mise à jour des dates pour {file_path} : {e}")

# Fonction principale pour parcourir les dossiers et fichiers
def update_dates_in_folders(root_folder):
    # Parcourt tous les dossiers à partir du répertoire racine
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)

        # Vérifie si le nom du dossier est une date au format "DD.MM.YYYY"
        if os.path.isdir(folder_path) and len(folder_name) == 10 and folder_name[2] == "." and folder_name[5] == ".":
            timestamp = date_string_to_timestamp(folder_name)
            if timestamp:
                # Parcourt les fichiers dans le dossier
                for file_name in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file_name)
                    # Vérifie si c'est un fichier image ou vidéo (extension classique)
                    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.mp4', '.mov', '.avi')):
                        # Met à jour la date du fichier avec le timestamp du nom du dossier
                        update_file_dates(file_path, timestamp)
                    else:
                        print(f"Fichier ignoré (pas une image ou vidéo) : {file_name}")

if __name__ == "__main__":
    update_dates_in_folders(root_folder)
