from multiprocessing import Pool
from datetime import datetime
import os


count_cpu = os.cpu_count()  # количество ядер (1 процесс = 1 ядро)


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for _ in file:
            if file.readline() != '':
                all_data.append(file.readline())


filename = [f'./file_test/file {number}.txt' for number in range(1, 5)]

start = datetime.now()

for i in filename:
    read_info(i)

end = datetime.now()

print(f'Время выполнения программы (линейно): {end - start}')  # 0:00:03.771115


# if __name__ == '__main__':
#     start = datetime.now()
#     with Pool(processes=count_cpu) as pool:
#         pool.map(read_info, filename)
#     end = datetime.now()
#
#     print(f'Время выполнения программы ({count_cpu} процесс(а)): {end - start}')  # 0:00:01.097504
