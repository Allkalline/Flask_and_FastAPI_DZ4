# Задание №5
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте процессы.


from multiprocessing import Process
from pathlib import Path


def file_read(file):
    with open(file, 'r', encoding='utf-8') as f:
        contents = f.read()
        print(f'В файле {file.name}: {len(contents.split())} слов')


def task5():
    dir_path = Path('files_for_tasks')
    files = [file for file in dir_path.iterdir() if file.is_file()]
    processes = []

    for file in files:
        p = Process(target=file_read, args=[file])
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


if __name__ == '__main__':
    task5()
