#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from collections import UserDict


class Pegs(UserDict):
    """
    >>> pegs = Pegs(2)
    >>> pegs
    {'A': [2, 1], 'B': [], 'C': []}
    >>> pegs.move_stack(2, "A", "C")
    >>> pegs
    {'A': [], 'B': [], 'C': [2, 1]}

    >>> pegs = Pegs(3)
    >>> pegs
    {'A': [3, 2, 1], 'B': [], 'C': []}
    >>> pegs.move_stack(3, "A", "C")
    >>> pegs
    {'A': [], 'B': [], 'C': [3, 2, 1]}

    >>> pegs = Pegs(4)
    >>> pegs
    {'A': [4, 3, 2, 1], 'B': [], 'C': []}
    >>> pegs.move_stack(4, "A", "C")
    >>> pegs
    {'A': [], 'B': [], 'C': [4, 3, 2, 1]}

    """

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

    def move_stack(self, ndisks: int, from_: str, to: str):
        aux = next(iter({"A", "B", "C"} - {from_, to}))
        if ndisks <= 1:
            self.move(from_, to)
        elif ndisks == 2:
            self.move(from_, aux)
            self.move(from_, to)
            self.move(aux, to)
        else:
            self.move_stack(ndisks - 1, from_=from_, to=aux)
            self.move(from_, to)
            self.move_stack(ndisks - 1, from_=aux, to=to)


def solve(ndisks: int) -> Pegs:
    """
    >>> solve(1)
    {'A': [], 'B': [], 'C': [1]}
    >>> solve(2)
    {'A': [], 'B': [], 'C': [2, 1]}
    >>> solve(3)
    {'A': [], 'B': [], 'C': [3, 2, 1]}
    """
    pegs = Pegs(ndisks)

    if ndisks == 1:
        pegs.move("A", "C")
    elif ndisks == 2:
        pegs.move_stack(2, "A", "C")
    elif ndisks == 3:
        nm1 = ndisks - 1
        pegs.move_stack(nm1, "A", "B")
        pegs.move("A", "C")
        pegs.move_stack(nm1, "B", "C")
    elif ndisks == 4:
        nm1 = ndisks - 1
        pegs.move_stack(nm1, "A", "B")
        pegs.move("A", "C")
        pegs.move_stack(nm1, "B", "C")
    else:
        raise ValueError(f"solve({ndisks}) not implemented")
    return pegs


if __name__ == "__main__":
    import doctest

    doctest.testmod()
