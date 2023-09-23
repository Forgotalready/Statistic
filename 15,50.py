from typing import List

import matplotlib.pyplot as plt
import random as rand

def getDistribution(n : int) -> List[List[float]]:
    dist = [rand.random() for x in range(n)]
    distForReturn = []

    for r in range(1, 11):
        distForReturn.append([])
    for r in range(1, 11):
        for x in dist:
            if (r - 1) / 10 < x <= r / 10:
                distForReturn[r - 1].append(x)

    return distForReturn

def main():
    n = 100
    dist = getDistribution(n)
    counts = [len(x) for x in dist]

    border = [(r - 1) / 10 for r in range(1, 12)]

    print(counts, border, sum(counts))

    plt.xticks(border)
    y, edges, _ = plt.hist(border[:-1], border , weights=counts)
    mid = 0.5 * (edges[1:] + edges[:-1])
    plt.plot(mid, y)
    plt.show()

if __name__ == "__main__":
    main()

