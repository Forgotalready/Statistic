import numpy as np
from typing import List, Tuple
import scipy.stats as st

SAMPLE = [13.8, 11.9, 11.5, 10.6, 13.9, 12.8, 12.5, 13.1, 12.0, 13.5, 11.7, 12.4, 11.9, 12.4, 13.7, 13.5]


def variance_interval_withoutMean(sample: np.array, gamma: float) -> Tuple:
    chi_r, chi_l = st.chi2.ppf([(1 - gamma) / 2, (1 + gamma) / 2], df=len(sample) - 1)
    var_noacc = np.var(sample)
    leftBorder = (len(sample) * (var_noacc ** 2)) / chi_l
    rightBorder = (len(sample) * (var_noacc ** 2)) / chi_r
    return (leftBorder, rightBorder)


def main():
    print(st.norm.interval(confidence=0.95, loc=np.mean(SAMPLE), scale=np.var(SAMPLE)))

    print(variance_interval_withoutMean(SAMPLE, 0.95))


if __name__ == '__main__':
    main()
