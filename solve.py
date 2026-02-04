#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from collections import UserDict
import unittest
import copy


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

    >>> pegs = Pegs(5)
    >>> pegs
    {'A': [5, 4, 3, 2, 1], 'B': [], 'C': []}
    >>> pegs.move_stack(5, "A", "C")
    >>> pegs
    {'A': [], 'B': [], 'C': [5, 4, 3, 2, 1]}

    >>> pegs = Pegs(6)
    >>> pegs
    {'A': [6, 5, 4, 3, 2, 1], 'B': [], 'C': []}
    >>> pegs.move_stack(6, "A", "C")
    >>> pegs
    {'A': [], 'B': [], 'C': [6, 5, 4, 3, 2, 1]}

    """

    def __init__(self, ndisks):
        data = {
            "A": list(range(ndisks, 0, -1)),
            "B": [],
            "C": [],
        }
        super().__init__(data)
        self.nsteps = 0

    def move(self, from_, to):
        src, dst = self.data[from_], self.data[to]
        if dst and src[-1] > dst[-1]:
            raise ValueError(f"Cannot place {src[-1]} on top {dst[-1]}")
        disk = src.pop()
        dst.append(disk)
        self.nsteps += 1

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


# def solve(ndisks: int) -> Pegs:
def solve(pegs: Pegs) -> int:
    pegs.move_stack(len(pegs["A"]), "A", "C")
    return pegs.nsteps


class TestSolve(unittest.TestCase):

    def test_solve10(self):
        expected_nsteps = {1: 1, 2: 3, 3: 7, 4: 15, 5: 31, 6: 63, 7: 127, 8: 255}
        for ndisks in range(1, 9):
            pegs = Pegs(ndisks)
            result = copy.copy(pegs["A"])
            nsteps = solve(pegs)
            self.assertEqual(pegs, {"A": [], "B": [], "C": result})
            self.assertEqual(nsteps, expected_nsteps[ndisks])


if __name__ == "__main__":
    unittest.main()
