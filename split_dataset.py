import sys
import numpy as np
import os
import json
import shutil
import json
def count_records(filepath):

    with open(filepath, 'r') as fp:
        nr=0
        for line in fp:
            nr += 1
    return nr-1


def split_dataset(data_path, splits=100):


    print("splits: ", splits)
    nr_of_records = count_records(data_path)
    print("nr_of_records: ", nr_of_records)
    data_file_splits = np.int32(np.rint(np.linspace(0, nr_of_records, splits+1)))



    testfolder = data_path.split("/")[-1].split(".")[0] + "_chunks"
    print("testfolder: ", testfolder)
    if os.path.isdir(testfolder):
        shutil.rmtree(testfolder)

    os.makedirs(testfolder)
    db_list = []
    chunk_index = 0
    old_split = chunk_index-1
    j = 0
    with open(data_path, 'r') as fp:

        for i, line in enumerate(fp):

            if i == 0:
                continue
            if j < data_file_splits[chunk_index + 1]:
                # print(line)
                db_list += [np.float32(line.split(","))]

            else:
                np.save(os.path.join(testfolder, str(chunk_index)), np.array(db_list))
                print("chunk index: ", chunk_index, "rows: ", old_split+1, " - ", i)
                old_split = i
                db_list = [np.float32(line.split(","))]
                chunk_index += 1
            j += 1

            # print("--")
        np.save(os.path.join(testfolder, str(chunk_index)), np.array(db_list))



    # python dictionary with key value pairs
    dict = {'nr_of_records': nr_of_records}

    # create json object from dictionary
    json_file = json.dumps(dict)

    # open file for writing, "w"
    f = open(os.path.join(testfolder,"meta_data.json"), "w")

    # write json object to file
    f.write(json_file)

    # close file
    f.close()

