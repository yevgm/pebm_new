
import numpy as np


def statistics(data_dict):

    stat_dict = {}
    for i in data_dict:
        data = data_dict[i]
        data = data[data != -1]
        if len(data)>0:
            mean_ = np.mean(data)
            median_ = np.median(data)
            min_ = np.amin(data)
            max_ = np.amax(data)
            q75, q25 = np.percentile(data, [75, 25])
            iqr_ = q75 - q25
            std_ = np.std(data)
            stat_dict[i] = {'mean': mean_, 'median': median_, 'min': min_, 'max': max_, 'iqr': iqr_, 'std': std_}
        else:
            stat_dict[i] = {'mean': -1, 'median': -1, 'min': -1, 'max': -1, 'iqr': -1, 'std': -1}

    return stat_dict

