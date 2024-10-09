import os
from PIL import Image

# Chemin du dossier contenant les images
dossier = '/chemin/vers/ton/dossier'

# Taille limite en octets (30 Ko = 30 * 1024 octets)
limite_taille = 30 * 1024

# Parcourir tous les fichiers dans le dossier
for fichier in os.listdir(dossier):
    chemin_fichier = os.path.join(dossier, fichier)
    
    # Vérifier si c'est un fichier et non un sous-dossier
    if os.path.isfile(chemin_fichier):
        try:
            # Ouvrir l'image pour vérifier si c'est bien une image
            with Image.open(chemin_fichier) as img:
                taille = os.path.getsize(chemin_fichier)
                
                # Si la taille du fichier est inférieure à la limite, on supprime
                if taille < limite_taille:
                    print(f"Suppression de {fichier}, taille : {taille} octets")
                    os.remove(chemin_fichier)
        except IOError:
            # Si le fichier ne peut pas être ouvert en tant qu'image, on ignore
            print(f"{fichier} n'est pas une image.")
