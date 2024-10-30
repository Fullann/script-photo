
# Script-Photo Documentation

## Script 1: Mise à jour des dates de création/modification des fichiers

### Étapes du script :
1. Il parcourt chaque dossier d'année (par exemple, 2020).
2. À l'intérieur de chaque dossier d'année, il parcourt les sous-dossiers de mois/jour (par exemple, 01.20).
3. Le script modifie les dates de création et de modification des fichiers dans ces sous-dossiers en fonction du nom du dossier parent (année et mois/jour).

### Explications détaillées :
- **Conversion de date** : Le nom du dossier au format `MM.JJ` est associé à l'année du dossier parent pour créer une date complète (année, mois, jour). Par exemple, si le dossier parent est `2020` et le sous-dossier est `01.20`, cela correspond au **20 janvier 2020**.
- **Mise à jour des fichiers** : Chaque fichier (image, vidéo, etc.) dans les sous-dossiers verra ses dates de modification et de création mises à jour en fonction du nom du dossier parent. Par exemple, les images/vidéos du sous-dossier `01.20` dans `2020` auront pour date de création le 20 janvier 2020.

### Comment utiliser le script :
1. **Chemin racine** : Modifiez la variable du script pour remplacer `"/chemin/vers/ton/dossier"` par le chemin de vos dossiers structurés par année.
2. **Exécution** : Exécutez le script dans un terminal avec la commande suivante :
   ```bash
   python ton_script.py
   ```

### Exemple de structure :
```text
/chemin/vers/ton/dossier/
    ├── 2020/
    │   ├── 01.20/
    │   │   ├── image1.jpg
    │   │   └── video1.mp4
    ├── 2021/
    │   ├── 05.12/
    │   │   ├── image2.jpg
    │   │   └── video2.mov
```

### Résultat :
- Le fichier `image1.jpg` et `video1.mp4` dans le dossier `01.20` seront mis à jour pour avoir leurs dates de création et de modification définies au **20 janvier 2020**.
- Le fichier `image2.jpg` et `video2.mov` dans le dossier `05.12` seront mis à jour pour le **12 mai 2021**.

---

## Script 2: Mise à jour des fichiers selon le nom du dossier (DD.MM.YYYY)

### Explications du script :
1. Le script recherche les dossiers nommés sous le format `DD.MM.YYYY`.
2. Il parcourt chaque fichier (image, vidéo) dans ces dossiers et extrait les dates du nom du dossier.
3. Il utilise cette information pour mettre à jour les dates de création et de modification des fichiers.

### Pré-requis :
Installez les bibliothèques Python suivantes avant d'exécuter le script :
- `pip install pillow` pour la gestion des images.
- `pip install pyexiv2` ou `pip install hachoir` pour modifier les métadonnées des fichiers (images et vidéos) de manière plus complète.

### Comment l'utiliser :
1. **Chemin racine** : Remplacez `"/chemin/vers/ton/dossier"` par le chemin de votre répertoire où se trouvent les dossiers datés.
2. **Exécution** : Exécutez ce script depuis un terminal avec la commande :
   ```bash
   python ton_script.py
   ```

### Fonctionnement détaillé :
- **Conversion de date** : Le nom du dossier (par exemple, `12.05.2021`) est converti en timestamp Unix via une fonction telle que `date_string_to_timestamp`.
- **Mise à jour des fichiers** : Chaque fichier (image, vidéo) dans ces dossiers voit ses dates de modification et de création mises à jour grâce à `os.utime`, qui permet de définir les dates des fichiers.

---

## Script 3: Suppression des fichiers en fonction de la taille

### Explications du script :
- Ce script parcourt les fichiers dans un dossier donné et vérifie s'ils sont des images.
- Il calcule la taille de chaque fichier en octets.
- Si un fichier pèse moins de 30 Ko (30 * 1024 octets), il est supprimé.
- Les fichiers non-images sont ignorés.

### Comment l'utiliser :
1. **Chemin du dossier** : Modifiez le chemin dans le script pour pointer vers le dossier à scanner.
2. **Exécution** : Exécutez le script avec la commande suivante :
   ```bash
   python ton_script.py
   ```

### Explication technique :
- Le script utilise `os.listdir()` pour lister les fichiers dans le dossier.
- Chaque fichier est vérifié pour s'assurer qu'il s'agit d'une image.
- Si la taille du fichier est inférieure à **30 Ko**, il est supprimé avec `os.remove()`.

## Script 4: Suppression des images strictement identiques dans un dossier et ses sous-dossiers
### Explications du script :
Ce script parcourt tous les sous-dossiers d'un répertoire donné pour identifier les images strictement identiques (même contenu binaire). Lorsqu'il trouve deux images identiques, l'une d'elles est supprimée pour ne conserver qu'un seul exemplaire de chaque image unique.

### Fonctionnement du script :
- Parcours des dossiers : Le script explore tous les sous-dossiers dans le dossier racine spécifié, en recherchant les images avec des extensions comme .png, .jpg, .jpeg, .bmp, et .gif.
- Calcul du hachage de chaque image : Pour chaque image, le script génère un hachage MD5 unique basé sur les données binaires de l'image. Ce hachage permet de vérifier si deux images sont strictement identiques.
- Détection des doublons et suppression : Si le hachage d'une image correspond à un hachage déjà enregistré, l'image est identifiée comme un doublon et supprimée.
### Explications techniques :
- Fonction image_hash : Cette fonction ouvre chaque image, la convertit en mode RGB (pour un formatage uniforme) et calcule un hachage MD5 unique basé sur les données binaires de l'image.
- Détection des doublons : Les hachages d'image sont stockés dans un dictionnaire (hashes). Si un hachage est déjà présent, le fichier est considéré comme un doublon et supprimé.
- Suppression : Pour chaque doublon détecté, le script utilise os.remove() pour le supprimer immédiatement.