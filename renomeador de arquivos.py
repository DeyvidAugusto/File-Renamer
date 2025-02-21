import os

def rename_files(directory, part_to_remove):
    for filename in os.listdir(directory):
        if part_to_remove in filename:
            new_filename = filename.replace(part_to_remove, '')
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f'Renamed: {filename} -> {new_filename}')

if __name__ == "__main__":
    directory = 'C:/Users/Uoufi/Downloads/exemplo'  # Troque o nome do diretório para o que deseja renomear
    part_to_remove = 'exemplo'  # Troque para a parte que deseja remover
    rename_files(directory, part_to_remove)