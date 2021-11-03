import pandas as pd
import numpy as np

from scipy.io import arff
from base.torchvision_dataset import TorchvisionDataset
from torch.utils.data import TensorDataset

class EP_Dataset(TorchvisionDataset):

    def __init__(self, root: str, normal_class):

        super().__init__(root)
        self.n_classes = 2

        # set up training set
        url1_train = '../data/epilepsy/EpilepsyDimension1_Train.arff'
        url2_train = '../data/epilepsy/EpilepsyDimension2_Train.arff'
        url3_train = '../data/epilepsy/EpilepsyDimension3_Train.arff'

        x_dim1_train, target_train = get_data(url1_train)
        x_dim2_train, __ = get_data(url2_train)
        x_dim3_train, __ = get_data(url3_train)
        row_train = x_dim1_train[:,0].shape
        column_train = x_dim1_train[0,:].shape

        x_final_train = np.dstack([x_dim1_train, x_dim2_train, x_dim3_train])
        y_final_train, index_train = get_target(target_train)

        train_set = TensorDataset(torch.Tensor(x_final_train), torch.Tensor(y_final_train), torch.Tensor(index_train))
        self.train_set = train_set

        # set up testing set
        url1_test = '../data/epilepsy/EpilepsyDimension1_Test.arff'
        url2_test = '../data/epilepsy/EpilepsyDimension2_Test.arff'
        url3_test = '../data/epilepsy/EpilepsyDimension3_Test.arff'

        x_dim1_test, target_test = get_data(url1_test)
        x_dim2_test, __ = get_data(url2_test)
        x_dim3_test, __ = get_data(url3_test)
        row_test = x_dim1_test[:,0].shape
        column_test = x_dim1_test[0,:].shape

        x_final_test = np.dstack([x_dim1_test, x_dim2_test, x_dim3_test])
        y_final_test, index_test = get_target(target_test)

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

# def get_labels(dim1, dim2, dim3, row, column):
#     """
#     This function combines 3 dimensions into one 3d array.
#     """
#     x_new = np.zeros([row, column])

#     for i in range(0, row):
#         for j in range(0, column):
#             #TODO
            


def get_target(y):
    """
    input: pandas series. last column of dataframe.
    This function converts the byte string of series and compare to each classification group
    Each class is represented as a number.
    output: returns numpy array of numbers and index array
    """
    y_new = []
    idx = []
    length = len(y)

    for i in range(0, length):
        if y[i].decode('UTF-8') == 'EPILEPSY':
            y_new.append(0)
        elif y[i].decode('UTF-8') == 'SAWING':
            y_new.append(1)
        elif y[i].decode('UTF-8') == 'RUNNING':
            y_new.append(2)
        elif y[i].decode('UTF-8') == 'WALKING':
            y_new.append(3)
        idx.append(i)

    return np.array(y_new), np.array(idx)