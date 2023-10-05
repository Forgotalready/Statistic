from typing import List
import numpy as np

DIST = [0.01, 0.29, 0.70, 1.01, 1.50, 2.46, 0.01, 0.42, 0.72, 1.01, 1.52, 2.50,
        0.04, 0.46, 0.76, 1.02, 1.54, 3.73, 0.17, 0.47, 0.78, 1.03, 1.59, 4.07,
        0.18, 0.47, 0.83, 1.05, 1.71, 6.03, 0.22, 0.56, 0.85, 1.32, 1.90, 0.22,
        0.59, 0.87, 1.34, 2.10, 0.25, 0.67, 0.93, 1.37, 2.35, 0.25, 0.68, 1.00,
        1.47, 2.46]

class SampleCharacteristics():
    def distMean(self, dist : List[float]) -> float:
        return (1/len(dist)) * (sum(dist))

    def distDisp(self, dist : List[float]) -> float:
        dist_mean = self.distMean(dist)
        return (1/len(dist)) * (sum([(x - dist_mean) ** 2 for x in dist]))

    def distQuantile(self, dist : List[float], q : List[float]) -> List[float]:
        return (np.quantile(DIST, q))

def main():
    print(SampleCharacteristics().distMean(DIST))
    print(SampleCharacteristics().distDisp(DIST))
    print(SampleCharacteristics().distQuantile(DIST, [0.25, 0.5, 0.75]))

if __name__ == "__main__":
    main()