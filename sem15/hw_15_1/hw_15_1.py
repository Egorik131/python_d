# Задание №6
# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
#   ○ имя файла без расширения или название каталога,
#   ○ расширение, если это файл,
#   ○ флаг каталога,
#   ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

from collections import namedtuple
from pathlib import Path
from logger import log_make

PATH = Path('C:\\', 'Users', 'Егор', 'PycharmProjects', 'python_deep', 'sem15', 'hw_15_1')
LOG_PATH = Path.cwd() / 'logfile.txt'


def obj_info(path: Path, logfile: Path):
    PathObject = namedtuple('PathObject', ('name', 'extension', 'flag_dir', 'parent'))
    parent = path.parts[-1]
    for item in path.iterdir():
        if item.is_file():
            name = item.name[:item.name.rfind('.')]
            extension = item.name[item.name.rfind('.') + 1:]
            log_make(PathObject(name, extension, item.is_dir(), parent), logfile)
        else:
            log_make(PathObject(name, extension, item.is_dir(), parent), logfile)


if __name__ == '__main__':
    obj_info(PATH, LOG_PATH)