import sys
import numpy as np
import os

def count_records(filepath):

    with open(filepath, 'r') as fp:
        for i, line in enumerate(fp):
            continue
    return i


if __name__ == '__main__':

    data_path = 'real_data/out0train.csv'
    splits = 100
    if len(sys.argv) >= 2:
        data_path = int(sys.argv[1])
    if len(sys.argv) >= 3:
        splits = int(sys.argv[2])
    print("splits: ", splits)
    nr_of_records = count_records(data_path)
    print("nr_of_records: ", nr_of_records)
    data_file_splits = np.int32(np.rint(np.linspace(0, nr_of_records, splits+1)))

    import shutil

    testfolder = data_path.split("/")[-1].split(".")[0] + "_chunks"
    print("testfolder: ", testfolder)
    if os.path.isdir(testfolder):
        shutil.rmtree(testfolder)

    os.makedirs(testfolder)
    db_list = []
    chunk_index = 0
    old_split = chunk_index-1
    with open(data_path, 'r') as fp:

        for i, line in enumerate(fp):

            if i == 0:
                continue
            if i < data_file_splits[chunk_index + 1]:
                # print(line)
                db_list += [np.float32(line.split(","))]

            else:
                np.save(os.path.join(testfolder, str(chunk_index)), np.array(db_list))
                print("chunk index: ", chunk_index, "rows: ", old_split+1, " - ", i)
                old_split = i
                db_list = []
                chunk_index += 1

            # print("--")
        np.save(os.path.join(testfolder, str(chunk_index)), np.array(db_list))