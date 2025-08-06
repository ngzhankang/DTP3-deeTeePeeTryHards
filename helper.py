import numpy as np
import pandas as pd
from typing import TypeAlias
from typing import Optional, Any    
Number: TypeAlias = int | float

def prepare_feature(np_feature):
    ones = np.ones((np_feature.shape[0], 1))
    return np.concatenate((ones, np_feature), axis=1)


#normalize using Z-score normalization
def normalize_z(array: np.ndarray, columns_means: Optional[np.ndarray]=None, 
                columns_stds: Optional[np.ndarray]=None) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
 
    # ensures array is a numpy array and not anything else to prevent possible errors
    if isinstance(array, pd.Series):
        array = array.to_frame()
    if isinstance(array, (pd.Series, pd.DataFrame)):
        array = array.to_numpy()

    # ensures columns_means and columns_stds follows the same number of columns as the input array
    assert columns_means is None or columns_means.shape == (1, array.shape[1])
    assert columns_stds is None or columns_stds.shape == (1, array.shape[1])
    if columns_means is None:
        columns_means = array.mean(axis=0).reshape(1,-1)
    if columns_stds is None:
        columns_stds = array.std(axis=0).reshape(1,-1)
    
    # running the formula for Z-score nomalization
    out = (array-columns_means) / columns_stds
    
    assert out.shape == array.shape
    assert columns_means.shape == (1, array.shape[1])
    assert columns_stds.shape == (1, array.shape[1])
    
    return out, columns_means, columns_stds


# computes the linear regression prediction (X*beta)
def calc_linreg(X, beta):
    result = np.matmul(X, beta)
    assert result.shape == (X.shape[0], 1)
    return result


# predicts target for multi-linear regression model given input features and model parameters (beta, means, stds)
def predict_linreg(array_feature, beta, means = None, stds = None):
    
    assert means is None or means.shape == (1, array_feature.shape[1])
    assert stds is None or stds.shape == (1, array_feature.shape[1])
    
    feature = prepare_feature(normalize_z(array_feature, means, stds)[0])
    result = calc_linreg(feature, beta)
    
    assert result.shape == (array_feature.shape[0], 1)
    return result