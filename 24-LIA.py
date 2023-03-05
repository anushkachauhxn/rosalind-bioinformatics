# 24) Independent Alleles
import sys
import os
from math import factorial as f


def nCr(n, r):
    return f(n) / (f(n-r) * f(r))


def getGenerationProbability(N, k):
    AaBb = 1/4  # Probability of AaBb for all combinations = 4/16
    n = 2**k  # total population of k-th generation

    # prob(atleast N) = prob(N) + prob(N+1) + ...
    prob = []
    for r in range(N, n+1):
        # binomial prob = nCx * p^x * q^(n-x)
        prob.append(nCr(n, r) * (AaBb ** r) * ((1-AaBb) ** (n-r)))
    return sum(prob)


def main():
    k, N = map(int, input().split())
    # probability that at least 'N' AaBb organisms will belong to the k-th generation
    print(getGenerationProbability(N, k))


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
