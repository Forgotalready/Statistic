import numpy as np
from typing import List, Tuple
import scipy.stats as st


def getSampling(mean : float, diviation : float, amount : int) -> np.array:
    return np.random.normal(mean, diviation, amount)


def variance_interval(sample : np.array, mean : np.float64, gamma : float) -> Tuple:
    T = sum([(x - mean) ** 2 for x in sample]) # вычисляем суммарное отклонение от среднего
    chi_r, chi_l = st.chi2.ppf([(1 - gamma) / 2, (1 + gamma) / 2], df=len(sample) - 1)

    leftBorder = T / chi_l
    rightBorder = T / chi_r
    return (leftBorder, rightBorder)


def variance_interval_withoutMean(sample: np.array, gamma: float) -> Tuple:
    chi_r, chi_l = st.chi2.ppf([(1 - gamma) / 2, (1 + gamma) / 2], df=len(sample) - 1)
    var_noacc = np.var(sample)
    leftBorder = (len(sample) * (var_noacc ** 2)) / chi_l
    rightBorder = (len(sample) * (var_noacc ** 2)) / chi_r
    return (leftBorder, rightBorder)


def main():
    sampl = getSampling(-1, 1, 20)

    print("Оценка среднего значения")
    print("Отклонение неизветсно: ", end="")
    print(st.t.interval(confidence=0.95, df=len(sampl) - 1, loc=np.mean(sampl), scale=np.var(sampl)))
    print("Отклонение известно: ", end="")
    print(st.norm.interval(confidence=0.95, loc=np.mean(sampl), scale=np.var(sampl)))

    print("Оценка диссперсии")
    print("Среднее известно", end = " ")
    print(variance_interval(sampl, np.mean(sampl), 0.95))
    print('Среднее неизветсно', end = " ")
    print(variance_interval_withoutMean(sampl, 0.95))


if __name__ == '__main__':
    main()
