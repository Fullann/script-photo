import os
import time
from datetime import datetime

# Chemin du répertoire racine où sont stockés les dossiers des années
root_folder = "/chemin/vers/ton/dossier"  # Remplace par le chemin correct

# Fonction pour convertir une chaîne de date "MM.JJ" en timestamp basé sur l'année donnée
def date_string_to_timestamp(year, month_day_str):
    try:
        # Combine l'année et le mois.jour pour créer une date complète
        date_str = f"{year}.{month_day_str}"
        return time.mktime(datetime.strptime(date_str, "%Y.%m.%d").timetuple())
    except ValueError:
        print(f"Format de date invalide pour : {month_day_str}")
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
    # Parcourt tous les dossiers représentant les années
    for year_folder in os.listdir(root_folder):
        year_folder_path = os.path.join(root_folder, year_folder)

        # Vérifie si c'est un dossier et si le nom est une année
        if os.path.isdir(year_folder_path) and year_folder.isdigit() and len(year_folder) == 4:
            year = year_folder

            # Parcourt les sous-dossiers représentant les dates au format "MM.JJ"
            for month_day_folder in os.listdir(year_folder_path):
                month_day_folder_path = os.path.join(year_folder_path, month_day_folder)

                # Vérifie si le nom du dossier est au format "MM.JJ"
                if os.path.isdir(month_day_folder_path) and len(month_day_folder) == 5 and month_day_folder[2] == ".":
                    timestamp = date_string_to_timestamp(year, month_day_folder)
                    if timestamp:
                        # Parcourt les fichiers dans le dossier "MM.JJ"
                        for file_name in os.listdir(month_day_folder_path):
                            file_path = os.path.join(month_day_folder_path, file_name)
                            # Vérifie si c'est un fichier image ou vidéo (extension classique)
                            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.mp4', '.mov', '.avi')):
                                # Met à jour la date du fichier avec le timestamp basé sur le nom du dossier
                                update_file_dates(file_path, timestamp)
                            else:
                                print(f"Fichier ignoré (pas une image ou vidéo) : {file_name}")

if __name__ == "__main__":
    update_dates_in_folders(root_folder)
