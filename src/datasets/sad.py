import pandas as pd
import numpy as np
import torch

from scipy.io import arff
from base.torchvision_dataset import TorchvisionDataset
from torch.utils.data import TensorDataset

class SAD_Dataset(TorchvisionDataset):

    def __init__(self, root: str, normal_class):

        super().__init__(root)
        self.n_classes = 2
        self.normal_class = normal_class

        # train set
        #load data file path
        url1_train = '../data/sad/SpokenArabicDigitsDimension1_TRAIN.arff'
        url2_train = '../data/sad/SpokenArabicDigitsDimension2_TRAIN.arff'
        url3_train = '../data/sad/SpokenArabicDigitsDimension3_TRAIN.arff'
        url4_train = '../data/sad/SpokenArabicDigitsDimension4_TRAIN.arff'
        url5_train = '../data/sad/SpokenArabicDigitsDimension5_TRAIN.arff'
        url6_train = '../data/sad/SpokenArabicDigitsDimension6_TRAIN.arff'
        url7_train = '../data/sad/SpokenArabicDigitsDimension7_TRAIN.arff'
        url8_train = '../data/sad/SpokenArabicDigitsDimension8_TRAIN.arff'
        url9_train = '../data/sad/SpokenArabicDigitsDimension9_TRAIN.arff'
        url10_train = '../data/sad/SpokenArabicDigitsDimension10_TRAIN.arff'
        url11_train = '../data/sad/SpokenArabicDigitsDimension11_TRAIN.arff'
        url12_train = '../data/sad/SpokenArabicDigitsDimension12_TRAIN.arff'
        url13_train = '../data/sad/SpokenArabicDigitsDimension13_TRAIN.arff'

        # get x and y as dataframe
        x_dim1_train, target_train = get_data(url1_train)
        x_dim2_train, __ = get_data(url2_train)
        x_dim3_train, __ = get_data(url3_train)
        x_dim4_train, __ = get_data(url4_train)
        x_dim5_train, __ = get_data(url5_train)
        x_dim6_train, __ = get_data(url6_train)
        x_dim7_train, __ = get_data(url7_train)
        x_dim8_train, __ = get_data(url8_train)
        x_dim9_train, __ = get_data(url9_train)
        x_dim10_train, __ = get_data(url10_train)
        x_dim11_train, __ = get_data(url11_train)
        x_dim12_train, __ = get_data(url12_train)
        x_dim13_train, __ = get_data(url13_train)

        x_dim1_train = get_features(x_dim1_train)
        x_dim2_train = get_features(x_dim2_train)
        x_dim3_train = get_features(x_dim3_train)
        x_dim4_train = get_features(x_dim4_train)
        x_dim5_train = get_features(x_dim5_train)
        x_dim6_train = get_features(x_dim6_train)
        x_dim7_train = get_features(x_dim7_train)
        x_dim8_train = get_features(x_dim8_train)
        x_dim9_train = get_features(x_dim9_train)
        x_dim10_train = get_features(x_dim10_train)
        x_dim11_train = get_features(x_dim11_train)
        x_dim12_train = get_features(x_dim12_train)
        x_dim13_train = get_features(x_dim13_train)

        # combine 13 dimensions of x
        x_train = np.dstack([x_dim1_train, x_dim2_train, x_dim3_train, x_dim4_train, x_dim5_train, x_dim6_train, x_dim7_train, x_dim8_train, x_dim9_train, x_dim10_train, x_dim11_train, x_dim12_train, x_dim13_train])
        # process output y and produce index
        y_train, index_train = get_target(target_train, normal_class)

        # train only on normal data, extracting normal data
        x_final_train, y_final_train, index_final_train = get_training_set(x_train, y_train, index_train)

        print("size: ", x_final_train.shape)
        train_set = TensorDataset(torch.Tensor(x_final_train), torch.Tensor(y_final_train), torch.Tensor(index_final_train))
        self.train_set = train_set

        # set up testing set
        url1_test = '../data/sad/SpokenArabicDigitsDimension1_TEST.arff'
        url2_test = '../data/sad/SpokenArabicDigitsDimension2_TEST.arff'
        url3_test = '../data/sad/SpokenArabicDigitsDimension3_TEST.arff'
        url4_test = '../data/sad/SpokenArabicDigitsDimension4_TEST.arff'
        url5_test = '../data/sad/SpokenArabicDigitsDimension5_TEST.arff'
        url6_test = '../data/sad/SpokenArabicDigitsDimension6_TEST.arff'
        url7_test = '../data/sad/SpokenArabicDigitsDimension7_TEST.arff'
        url8_test = '../data/sad/SpokenArabicDigitsDimension8_TEST.arff'
        url9_test = '../data/sad/SpokenArabicDigitsDimension9_TEST.arff'
        url10_test = '../data/sad/SpokenArabicDigitsDimension10_TEST.arff'
        url11_test = '../data/sad/SpokenArabicDigitsDimension11_TEST.arff'
        url12_test = '../data/sad/SpokenArabicDigitsDimension12_TEST.arff'
        url13_test = '../data/sad/SpokenArabicDigitsDimension13_TEST.arff'

        x_dim1_test, target_test = get_data(url1_test)
        x_dim2_test, __ = get_data(url2_test)
        x_dim3_test, __ = get_data(url3_test)
        x_dim4_test, __ = get_data(url4_test)
        x_dim5_test, __ = get_data(url5_test)
        x_dim6_test, __ = get_data(url6_test)
        x_dim7_test, __ = get_data(url7_test)
        x_dim8_test, __ = get_data(url8_test)
        x_dim9_test, __ = get_data(url9_test)
        x_dim10_test, __ = get_data(url10_test)
        x_dim11_test, __ = get_data(url11_test)
        x_dim12_test, __ = get_data(url12_test)
        x_dim13_test, __ = get_data(url13_test)

        x_dim1_test = get_features(x_dim1_test)
        x_dim2_test = get_features(x_dim2_test)
        x_dim3_test = get_features(x_dim3_test)
        x_dim4_test = get_features(x_dim4_test)
        x_dim5_test = get_features(x_dim5_test)
        x_dim6_test = get_features(x_dim6_test)
        x_dim7_test = get_features(x_dim7_test)
        x_dim8_test = get_features(x_dim8_test)
        x_dim9_test = get_features(x_dim9_test)
        x_dim10_test = get_features(x_dim10_test)
        x_dim11_test = get_features(x_dim11_test)
        x_dim12_test = get_features(x_dim12_test)
        x_dim13_test = get_features(x_dim13_test)

        x_final_test = np.dstack([x_dim1_test, x_dim2_test, x_dim3_test, x_dim4_test, x_dim5_test, x_dim6_test, x_dim7_test, x_dim8_test, x_dim9_test, x_dim10_test, x_dim11_test, x_dim12_test, x_dim13_test])
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

def get_features(x):
    """
    input: unprocessed features data
    This function replaces missing values with zeroes.
    output: processed features data
    """
    for i in range(0, len(x)):
        for j in range(0, 93):
            if pd.isna(x[i][j]):
                x[i][j] = 0
    
    return x


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
        if y[i].decode('UTF-8') == '1':
            y_temp.append(0)
        elif y[i].decode('UTF-8') == '2':
            y_temp.append(1)
        elif y[i].decode('UTF-8') == '3':
            y_temp.append(2)
        elif y[i].decode('UTF-8') == '4':
            y_temp.append(3)
        elif y[i].decode('UTF-8') == '5':
            y_temp.append(4)
        elif y[i].decode('UTF-8') == '6':
            y_temp.append(5)
        elif y[i].decode('UTF-8') == '7':
            y_temp.append(6)
        elif y[i].decode('UTF-8') == '8':
            y_temp.append(7)
        elif y[i].decode('UTF-8') == '9':
            y_temp.append(8)
        elif y[i].decode('UTF-8') == '10':
            y_temp.append(9)
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
