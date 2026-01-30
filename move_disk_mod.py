#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


Peg = list[int]
NDISKS = 3
from_: Peg = [*range(NDISKS, 0, -1)]
to: Peg = []
aux: Peg = []

PEGS = {
    "A": [3, 2, 1],
    "B": [],
    "C": [],
}


def move(from_, to, pegs=PEGS):
    src, dst = pegs[from_], pegs[to]
    if dst and src[-1] > dst[-1]:
        raise ValueError(f"Cannot place {src[-1]} on top {dst[-1]}")
    disk = src.pop()
    dst.append(disk)


def solve3():
    """
    >>> solve3()
    >>> PEGS["A"]
    []
    >>> PEGS["C"]
    [3, 2, 1]
    >>> PEGS["B"]
    []
    >>>
    """
    move("A", "C")
    move("A", "B")
    move("C", "B")
    move("A", "C")
    move("B", "A")
    move("B", "C")
    move("A", "C")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
