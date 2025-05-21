import os
import shutil
from zipfile import zipfile
import pytest


@pytest.fixture(scope="function")
def create_directory():
    CURRENT_FILE = os.path.abspath(__file__) # получаем путь к текущему файлу
    CURRENT_DIR = os.path.dirname(CURRENT_FILE) # по файлу находим путь к папке, где он лежит
    if not os.path.exists("resource"):
        os.mkdir("resource")
    #TMP_DIR = os.path.join(CURRENT_DIR, "resource")

    yield
    shutil.rmtree(os.path.join(CURRENT_DIR, "resource"))


