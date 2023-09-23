import matplotlib.pyplot as plt

DIST = [0.01, 0.29, 0.70, 1.01, 1.50, 2.46, 0.01, 0.42, 0.72, 1.01, 1.52, 2.50, 0.04, 0.46, 0.76, 1.02, 1.54, 3.73,
        0.17, 0.47, 0.78, 1.03, 1.59, 4.07, 0.18, 0.47, 0.83, 1.05, 1.71, 6.03, 0.22, 0.56, 0.85, 1.32, 1.90, 0.22,
        0.59, 0.87, 1.34, 2.10, 0.25, 0.67, 0.93, 1.37, 2.35, 0.25, 0.68, 1.00, 1.47, 2.46]


def printFunc():
    global DIST
    from statsmodels.distributions.empirical_distribution import ECDF
    func = ECDF(DIST)

    plt.step(func.x, func.y)
    plt.ylabel('$F(x)$'); plt.xlabel('$x$')
    plt.show()

def printMedian():
    global DIST
    dist = sorted(DIST)
    print(dist[len(dist) // 2])

def printGist():
    global DIST
    dist = sorted(DIST)
    border = [0]
    r = 1

    while r < dist[-1]:
        border.append(r)
        r += 1
    border.append(r)

    counters = [0] * (len(border) - 1)
    for i in range(len(border) - 1):
        for x in dist:
            if border[i] < x <= border[i + 1]:
                counters[i] += 1

    y, edges, _ = plt.hist(border[:-1], border, weights=counters)
    mid = 0.5 * (edges[1:] + edges[:-1])
    plt.plot(mid, y)
    plt.show()


def main():
    q = input()
    if q == 'func':
        printFunc()
    elif q == 'gist':
        printGist()
    elif q == 'median':
        printMedian()


if __name__ == '__main__':
    main()
