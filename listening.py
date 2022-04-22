from shutil import copytree
from threading import Thread
import os
from time import sleep, perf_counter

import console_args


class Listening:
    def __init__(self, path_start: str = ..., path_end: str = ...):
        self.path_start = path_start
        self.path_end = path_end

    @staticmethod
    def copy(path1, path2):
        copytree(path1, path2, dirs_exist_ok=True)

    def copy_to_folder(self):
        print(f'''  Copy file :
        [from] \t {self.path_start}
        [to] \t {self.path_end}
        ''')

        files = os.listdir(self.path_start)

        for file in files:
            filename, extention = os.path.splitext(file)
            extention = extention[1:]

            if extention == '':
                t1 = Thread(target=self.copy, args=(self.path_start + f'/{filename}', self.path_end + f'/{filename}'))
                t1.start()

            else:
                copytree(self.path_start, self.path_end, dirs_exist_ok=True)

    def listening_on_folder(self):
        print(f'''  Listening to : 
        [from] \t {self.path_start}
        [to] \t {self.path_end}
        ''')

        start = perf_counter()

        try:
            while True:
                copytree(self.path_start, self.path_end, dirs_exist_ok=True)

                sleep(2)
                continue

            end = perf_counter()

            print(f'Listening continued : {round(end - start, 2)}s.')
            return 0

        except KeyboardInterrupt:
            end = perf_counter()
            print(f'Listening continued : {round(end - start, 2)}s.')


def main():
    args = console_args.main()

    listening = Listening(args.Start_Path, args.End_Path)
    match args.infinity:
        case False:
            listening.copy_to_folder()

        case True:
            listening.listening_on_folder()

        case _:
            print('That\'s  not good ;)')


if __name__ == '__main__':
    main()
