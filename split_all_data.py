import os
from split_dataset import split_dataset


if __name__ == '__main__':

    for file in os.listdir('real_data'):

        if file.endswith('.csv'):
            print("file name: ", file)
            split_dataset(os.path.join('real_data',file))