import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            all_data.extend(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

start = datetime.datetime.now()
for i in range(1, 5):
    read_info(f'file {i}.txt')
end = datetime.datetime.now()

print(end - start) # результат составил 0:00:08.329394

# if __name__  == '__main__':
#     start = datetime.datetime.now()
#     with multiprocessing.Pool(processes=6) as pool:
#         pool.map(read_info, filenames)
#     end = datetime.datetime.now()
#     print(end - start) # результат составил 0:00:08.983872
