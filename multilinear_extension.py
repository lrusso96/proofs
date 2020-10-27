"""
Fix some prime p of your choosing. Write a Python program that takes as input an array of length 2^l specifying all evaluations of a function f:{0,1} → Fp and a vector r ∈ Fp and outputs f'(r).
"""

from typing import Dict, List
from itertools import product


def binaries(n):
    return list(map(list, product([0, 1], repeat=n)))


def prettify(l):
    return ",".join(map(str, l))


def CTW11(p: int, l: int, evaluations: List[int], r: List[int]) -> int:
    """[CTW11]

    Initializes f'(r) = 0, and processes each update (w,f(w)) via:
        * f'(r) ← f'(r) + f(w)·χw(r)

    Args:
        p (int): Prime number for Fp.
        l (int): Length of input value for f.
        evaluations (List[int]): All evaluations of f.
        r (List[int]): The evaluation point of f' that needs to be computed.

    Cost:
        * O(n logn) time
        * O(logn) space
    """

    if 2**l != len(evaluations):
        print(f"You need to specify {2**l} values")
        exit(1)

    def chi(w: List[int], x: List[int]):
        if len(w) != len(x):
            print(
                f"Cannot compute χw(x): w has length {len(w)} and x has length {len(x)}.")
            exit(1)
        pi = 1
        for i in range(len(r)):
            pi *= (x[i]*w[i] + (1 - x[i])*(1-w[i]))
            pi = pi % p
        return pi

    ret = 0
    ctr = 0
    for w in binaries(l):
        ret += evaluations[ctr]*chi(w, r)
        ret = ret % p
        ctr += 1
    return ret


"""[VSBW13]

TODO Implement it.
"""


if __name__ == "__main__":
    p = int(input("Insert a prime value p: "))
    l = int(input("Insert length l: "))
    evaluations = [int(input(f"f({prettify(i)}): ")) for i in binaries(l)]

    r = [int(input(f"r{i}: ")) for i in range(l)]

    output = CTW11(p, l, evaluations, r)
    print(f"The output f'({prettify(r)}) is: {output}")
