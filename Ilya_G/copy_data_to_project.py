import os
import shutil
import MMpy

def copy_data_to_project(path_project,network_path,var,ignored_names):
    # Создаем папку Сетевая папка в проете Майкромайн
    if not os.path.isdir(path_project):
        os.mkdir(path_project)

    # Удаляем все файлы из проекта из папки Сетевая папка
    if var:
        shutil.rmtree(path_project)  # Удаляем всю директорию из проекта
        shutil.copytree(network_path, path_project,
                        ignore=ignored_names, dirs_exist_ok=True)

    else:
        print("FDFDFDF")