import os
import piexif
from PIL import Image
import datetime

def update_exif_date(image_path, new_date):
    # Ouvrir l'image
    img = Image.open(image_path)
    
    # Extraire les données EXIF
    exif_dict = piexif.load(img.info["exif"])

    # Convertir la nouvelle date en format EXIF (YYYY:MM:DD HH:MM:SS)
    new_exif_date = new_date.strftime('%Y:%m:%d %H:%M:%S')
    
    # Mettre à jour la date de prise de vue
    exif_dict['0th'][piexif.ImageIFD.DateTime] = new_exif_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_exif_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_exif_date

    # Convertir les données EXIF mises à jour en format binaire
    exif_bytes = piexif.dump(exif_dict)

    # Enregistrer l'image avec les nouveaux EXIF
    img.save(image_path, exif=exif_bytes)

    print(f"Date de prise de vue mise à jour pour {image_path} : {new_exif_date}")

def update_exif_for_directory(directory_path, new_date):
    # Parcourir tous les fichiers dans le dossier
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        # Vérifier si c'est une image (vous pouvez ajouter d'autres extensions si nécessaire)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff')):
            update_exif_date(file_path, new_date)

# Exemple d'utilisation
directory_path = "./nouvelle ans"  # Remplacez par le chemin de votre dossier d'images
new_date = datetime.datetime(2024, 12, 31, 22, 30, 0)  # Nouvelle date : 21 février 2025, 14h30
update_exif_for_directory(directory_path, new_date)
