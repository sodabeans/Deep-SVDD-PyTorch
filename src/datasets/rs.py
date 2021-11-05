import pandas as pd
import numpy as np
import torch

from scipy.io import arff
from base.torchvision_dataset import TorchvisionDataset
from torch.utils.data import TensorDataset

class RS_Dataset(TorchvisionDataset):

    def __init__(self, root: str, normal_class):

        super().__init__(root)
        self.n_classes = 2
        self.normal_class = normal_class

        # train set
        #load data file path
        url1_train = '../data/rs/RacketSportsDimension1_TRAIN.arff'
        url2_train = '../data/rs/RacketSportsDimension2_TRAIN.arff'
        url3_train = '../data/rs/RacketSportsDimension3_TRAIN.arff'
        url4_train = '../data/rs/RacketSportsDimension4_TRAIN.arff'
        url5_train = '../data/rs/RacketSportsDimension5_TRAIN.arff'
        url6_train = '../data/rs/RacketSportsDimension6_TRAIN.arff'

        # get x and y as dataframe
        x_dim1_train, target_train = get_data(url1_train)
        x_dim2_train, __ = get_data(url2_train)
        x_dim3_train, __ = get_data(url3_train)
        x_dim4_train, __ = get_data(url4_train)
        x_dim5_train, __ = get_data(url5_train)
        x_dim6_train, __ = get_data(url6_train)

        # combine 6 dimensions of x
        x_train = np.dstack([x_dim1_train, x_dim2_train, x_dim3_train, x_dim4_train, x_dim5_train, x_dim6_train])
        # process output y and produce index
        y_train, index_train = get_target(target_train, normal_class)

        # train only on normal data, extracting normal data
        x_final_train, y_final_train, index_final_train = get_training_set(x_train, y_train, index_train)

        # print("size: ", x_final_train.shape)
        train_set = TensorDataset(torch.Tensor(x_final_train), torch.Tensor(y_final_train), torch.Tensor(index_final_train))
        self.train_set = train_set

        # set up testing set
        url1_test = '../data/rs/RacketSportsDimension1_TEST.arff'
        url2_test = '../data/rs/RacketSportsDimension2_TEST.arff'
        url3_test = '../data/rs/RacketSportsDimension3_TEST.arff'
        url4_test = '../data/rs/RacketSportsDimension4_TEST.arff'
        url5_test = '../data/rs/RacketSportsDimension5_TEST.arff'
        url6_test = '../data/rs/RacketSportsDimension6_TEST.arff'

        x_dim1_test, target_test = get_data(url1_test)
        x_dim2_test, __ = get_data(url2_test)
        x_dim3_test, __ = get_data(url3_test)
        x_dim4_test, __ = get_data(url4_test)
        x_dim5_test, __ = get_data(url5_test)
        x_dim6_test, __ = get_data(url6_test)

        x_final_test = np.dstack([x_dim1_test, x_dim2_test, x_dim3_test, x_dim4_test, x_dim5_test, x_dim6_test])
        y_final_test, index_test = get_target(target_test, normal_class)

        test_set = TensorDataset(torch.Tensor(x_final_test), torch.Tensor(y_final_test), torch.Tensor(index_test))
        self.test_set = test_set


def get_data(url):
    """
    input: path to arff data file
    This function loads the arff file, then converts into dataframe.
    The dataframe is then split into x and y.
    output: x is dataframe object without the last column. y is series.
    """
    loaded = arff.loadarff(url)
    df = pd.DataFrame(loaded[0])
    
    # dropping the last column of dataframe
    # it is still a dataframe object
    x = df.iloc[:, :-1].to_numpy()

    # getting last column as series, not dataframe object
    # as dataframe object is using iloc[:, -1:]
    y = df.iloc[:, -1]

    return x, y


def get_target(y, normal_class):
    """
    input: pandas series. last column of dataframe.
    This function converts the byte string of series and compare to each classification group
    Each class is represented as a number.
    output: returns numpy array of numbers and index array
    """
    y_new = []
    y_temp = []
    idx = []
    length = len(y)

    for i in range(0, length):
        if y[i].decode('UTF-8') == 'Badminton_Smash':
            y_temp.append(0)
        elif y[i].decode('UTF-8') == 'Badminton_Clear':
            y_temp.append(1)
        elif y[i].decode('UTF-8') == 'Squash_ForehandBoast':
            y_temp.append(2)
        elif y[i].decode('UTF-8') == 'Squash_BackhandBoast':
            y_temp.append(3)
        idx.append(i)

    for i in range(0, length):
        if y_temp[i] == normal_class:
            y_new.append(0) # normal
        else:
            y_new.append(1) # anomaly

    return np.array(y_new), np.array(idx)

def get_training_set(x, y, idx):
    """
    Input: x, y, index of training set from data file
    This function only collects the normal data from train set.
    The model only trains on normal data of the train set.
    Output: x, y, index of normal data only in train set.
    """
    x_final = []
    y_final = []
    idx_final = []

    for i in range(0, len(x)):
        if y[i] == 0:
            x_final.append(x[i])
            y_final.append(y[i])
    
    for i in range(0, len(x_final)):
        idx_final.append(i)
    
    return np.array(x_final), np.array(y_final), np.array(idx_final)
