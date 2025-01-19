import os
import shutil

def merge_datasets(dataset1_path, dataset2_path, output_path):
    """
    Fusionne deux datasets en prenant uniquement les dossiers communs.

        dataset1_path (str): Chemin du premier dataset.
        dataset2_path (str): Chemin du deuxième dataset.
        output_path (str): Chemin du dossier de sortie.
    """
    
# Vérification des chemins
    if os.path.exists(dataset1_path):
        print(f"Chemin du premier dataset existe : {dataset1_path}")
    else:
        print(f"Chemin du premier dataset n'existe pas : {dataset1_path}")

    if os.path.exists(dataset2_path):
        print(f"Chemin du deuxième dataset existe : {dataset2_path}")
    else:
        print(f"Chemin du deuxième dataset n'existe pas : {dataset2_path}")

    if os.path.exists(output_path):
        print(f"Chemin du dossier de sortie existe déjà : {output_path}")
    else:
        print(f"Chemin du dossier de sortie sera créé : {output_path}")

    # Obtenir la liste des dossiers pour chaque dataset
    dataset1_folders = set(os.listdir(dataset1_path))
    dataset2_folders = set(os.listdir(dataset2_path))

    # Identifier les dossiers en commun
    common_folders = dataset1_folders.intersection(dataset2_folders)

    # Créer le dossier de sortie s'il n'existe pas
    os.makedirs(output_path, exist_ok=True)

    for folder in common_folders:
        folder_path1 = os.path.join(dataset1_path, folder)
        folder_path2 = os.path.join(dataset2_path, folder)
        output_folder_path = os.path.join(output_path, folder)

        # Créer le dossier de sortie pour ce Pokémon
        os.makedirs(output_folder_path, exist_ok=True)

        # Copier les images du premier dataset
        for file in os.listdir(folder_path1):
            
            source_file = os.path.join(folder_path1, file)
            dest_file = os.path.join(output_folder_path, file)
            shutil.copy2(source_file, dest_file)

        # Copier les images du deuxième dataset
        for file in os.listdir(folder_path2):
            source_file = os.path.join(folder_path2, file)
            dest_file = os.path.join(output_folder_path, file)

            # Éviter les doublons en cas de fichiers avec le même nom
            if os.path.exists(dest_file):
                file_name, file_ext = os.path.splitext(file)
                dest_file = os.path.join(output_folder_path, f"{file_name}_from_dataset2{file_ext}")

            shutil.copy2(source_file, dest_file)


