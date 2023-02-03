from torch.utils.data import Dataset
import numpy as np
import os

class CustomDataset(Dataset):
    """Face Landmarks dataset."""

    def __init__(self, data_path, nr_of_records, nr_of_splits):
        """
        Args:
            csv_file (string): Path to the csv file with annotations.

        """
        self.len = nr_of_records
        self.data_path = data_path
        self.data_file_splits = np.int32(np.rint(np.linspace(0, nr_of_records, nr_of_splits + 1)))

    def __len__(self):
        return self.len

    def __getitem__(self, idx):
        chunk = np.where((idx >= self.data_file_splits[:-1]) * (idx < self.data_file_splits[1:]))[0][0]
        sample = np.load(os.path.join(self.data_path, str(chunk) + '.npy'))[idx - self.data_file_splits[chunk]]
        X = np.expand_dims(sample[:-1], 1)
        X /= 255
        y = sample[-1]

        return X, y
