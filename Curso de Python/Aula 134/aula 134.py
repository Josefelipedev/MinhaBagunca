import os
import shutil

caminho_original = ''
caminho_novo = ''

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')


for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        # if '.str' in file:
        #     os.remove(new_file_path)

        if '.srt' in file:
            shutil.copy(old_file_path, new_file_path)
            print(f'Arquivo {file} copiado com sucesso.')
        shutil.move(old_file_path, new_file_path)
        print(f'Arquivo {file} movido com sucesso.')