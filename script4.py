import os
import hashlib
from PIL import Image

def image_hash(image_path):
    """Calcule le hachage MD5 d'une image pour la comparer."""
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        md5_hash = hashlib.md5(img.tobytes())
        return md5_hash.hexdigest()

def find_and_remove_duplicates(folder_path):
    """Recherche et supprime les images identiques dans un dossier et ses sous-dossiers."""
    hashes = {}
    duplicates = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                file_path = os.path.join(root, file)
                
                # Calculer le hachage de l'image
                img_hash = image_hash(file_path)
                
                # Vérifie si ce hachage existe déjà
                if img_hash in hashes:
                    duplicates.append(file_path)
                    print(f"Doublon trouvé et supprimé : {file_path}")
                    os.remove(file_path)  # Supprime l'image en doublon
                else:
                    hashes[img_hash] = file_path

    if duplicates:
        print(f"{len(duplicates)} doublons supprimés.")
    else:
        print("Aucun doublon trouvé.")

# Exemple d'utilisation
find_and_remove_duplicates("chemin/vers/votre/dossier")
