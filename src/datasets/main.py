from .mnist import MNIST_Dataset
from .cifar10 import CIFAR10_Dataset
from .ct import CT_Dataset
from .ep import EP_Dataset


def load_dataset(dataset_name, data_path, normal_class):
    """Loads the dataset."""

    implemented_datasets = ('mnist', 'cifar10', 'ct', 'ep')
    assert dataset_name in implemented_datasets

    dataset = None

    if dataset_name == 'mnist':
        dataset = MNIST_Dataset(root=data_path, normal_class=normal_class)

    if dataset_name == 'cifar10':
        dataset = CIFAR10_Dataset(root=data_path, normal_class=normal_class)

    if dataset_name == 'ct':
        dataset = CT_Dataset(root=data_path, normal_class=normal_class)
    
    if dataset_name == 'ep':
        dataset = EP_Dataset(root=data_path, normal_class=normal_class)

    return dataset
