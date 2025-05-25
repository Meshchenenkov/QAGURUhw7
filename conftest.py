import os
import pytest
import zipfile
import shutil

CURRENT_FILE = os.path.abspath(__file__) # путь к файлу
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE) # по файлу находим путь к папке, где он лежит
RESOURCES_DIRECTORY = os.path.join(CURRENT_DIRECTORY, 'resources') # путь к папке 'resources'
FILES_DIRECTORY = os.path.join(CURRENT_DIRECTORY, "files") # путь к папке 'files'

@pytest.fixture(scope="function", autouse=True)
def create_directory_with_zipfile():
    if not os.path.exists(RESOURCES_DIRECTORY):
        os.mkdir(RESOURCES_DIRECTORY)
    ZIP_FILE = os.path.join(RESOURCES_DIRECTORY, 'zip.zip') #путь к зип-архиву
    with zipfile.ZipFile(ZIP_FILE, 'w') as zf:  # создаем архив
        for file in ['csv.csv', 'pdf.pdf', 'xlsx.xlsx']:  # выбираем файлы для добавления в архив
            add_file = os.path.join(FILES_DIRECTORY, file)  # склеиваем путь к файлам которые добавляют в архив
            zf.write(add_file, os.path.basename(add_file))  # добавляем файлы в архив
    yield
    if os.path.exists(RESOURCES_DIRECTORY):
        shutil.rmtree(RESOURCES_DIRECTORY)


