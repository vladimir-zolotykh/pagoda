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

    def move_stack(self, ndisks):
        if ndisks <= 1:
            self.move("A", "C")
        elif ndisks == 2:
            self.move("A", "B")
            self.move("A", "C")
            self.move("B", "C")
        else:
            self.move_stack(ndisks - 1, from_="A", to="B", aux="C")
            self.move("A", "C")
            self.move_stack(ndisks - 1, from_="B", to="C", aux="A")


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
        pegs.move("A", "B")
        pegs.move("A", "C")
        pegs.move("B", "C")
    elif ndisks == 3:
        pegs.move("A", "C")
        pegs.move("A", "B")
        pegs.move("C", "B")
        pegs.move("A", "C")
        pegs.move("B", "A")
        pegs.move("B", "C")
        pegs.move("A", "C")
    elif ndisks == 4:
        pegs.move_stack(3, "A", "B", aux="C")
        pegs.move("A", "C")
        pegs.move_stack(3, "B", "C", aux="A")
    else:
        raise ValueError(f"solve({ndisks}) not implemented")
    return pegs


if __name__ == "__main__":
    import doctest

    doctest.testmod()
