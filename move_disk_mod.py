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


def solve3(
    ndisks: int, pegs: Pegs, from_: str = "A", to: str = "C", aux: str = "B"
) -> None:
    """
    >>> pegs = Pegs(3)
    >>> solve3(3, pegs, "A", "C", "B")
    >>> pegs["A"]
    []
    >>> pegs["C"]
    [3, 2, 1]
    >>> pegs["B"]
    []
    >>>
    """
    pegs3 = {"A", "B", "C"}
    pegs3 -= {from_, to}
    assert aux == next(iter(pegs3)), f"'aux' must be {aux}"
    pegs.move(from_, to)
    pegs.move(from_, aux)
    pegs.move(to, aux)
    pegs.move(from_, to)
    pegs.move(aux, from_)
    pegs.move(aux, to)
    pegs.move(from_, to)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
