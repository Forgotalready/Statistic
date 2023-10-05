from typing import List

v = [2, 4, 3, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 3]
ksi1_global = [23.0, 24.0, 24.5, 24.5, 25.0, 25.5, 26.0, 26.0, 26.0, 26.5, 26.5, 27.0, 27.0, 28.0]
ksi2_global = [0.48, 0.50, 0.49, 0.50, 0.51, 0.52, 0.49, 0.51, 0.53, 0.50, 0.52, 0.54, 0.52, 0.52]

def distMean(dist : List[float], freq : List[int]) -> float:
    return (1. / sum(freq)) * sum([a * float(t) for a, t in zip(dist, freq)])

def linTransform(a: float, b: float, dist: List[float]) -> List[float]:
    return [((x - a) / b) for x in dist]

def distDisp(dist : List[float], freq : List[int]) -> float:
    dist_mean = distMean(dist, freq)
    return (1. / sum(freq)) * sum([((a - dist_mean) ** 2) * float(t) for a, t in zip(dist, freq)])

def distCov(ksi1 : List[float], ksi2 : List[float], freq : List[int]) -> float:
    ksi1_mean = distMean(ksi1, freq)
    ksi2_mean = distMean(ksi2, freq)
    return (1. / sum(freq)) * sum([(x - ksi1_mean) * (y - ksi2_mean) * float(z) for x, y, z in zip(ksi1, ksi2, freq)])

def distKor(ksi1 : List[float], ksi2 : List[float], freq : List[int]) -> float:
    return distCov(ksi1, ksi2, freq) / ((distDisp(ksi1, freq) * distDisp(ksi2, freq)) ** (1/2))


def main():
    ksi1_transform = linTransform(26.0, 0.5, ksi1_global)
    ksi2_transform = linTransform(0.50, 0.01, ksi2_global)
    # pho_n = S_12 / S1S2
    print(sum(v))
    print(distKor(ksi1_transform, ksi2_transform, v))
    print(distKor(ksi1_global, ksi2_global, v))


if __name__ == '__main__':
    main()
