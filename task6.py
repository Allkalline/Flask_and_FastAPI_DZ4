# Задание №6
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте асинхронный подход.


import asyncio
from pathlib import Path


async def file_read(file):
    with open(file, 'r', encoding='utf-8') as f:
        contents = f.read()
        print(f'В файле {file.name}: {len(contents.split())} слов')


async def task6():
    dir_path = Path('files_for_tasks')
    files = [file for file in dir_path.iterdir() if file.is_file()]
    tasks = [asyncio.create_task(file_read(file)) for file in files]

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(task6())
