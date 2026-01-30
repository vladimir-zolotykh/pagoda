#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from collections import UserDict


class Pegs(UserDict):
    def __init__(self, ndisks):
        data = {
            "A": list(range(ndisks, 0, -1)),
            "B": [],
            "C": [],
        }
        super().__init__(data)

    def move(self, from_, to):
        src, dst = self.data[from_], self.data[to]
        if dst and src[-1] > dst[-1]:
            raise ValueError(f"Cannot place {src[-1]} on top {dst[-1]}")
        disk = src.pop()
        dst.append(disk)


def solve3(pegs: Pegs) -> Pegs:
    """
    >>> pegs = Pegs(3)
    >>> solve3(pegs)
    >>> pegs["A"]
    []
    >>> pegs["C"]
    [3, 2, 1]
    >>> pegs["B"]
    []
    >>>
    """
    pegs.move("A", "C")
    pegs.move("A", "B")
    pegs.move("C", "B")
    pegs.move("A", "C")
    pegs.move("B", "A")
    pegs.move("B", "C")
    pegs.move("A", "C")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
