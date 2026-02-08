#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from collections import UserDict
import unittest
import copy


class Pegs(UserDict):
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

    def solve(self, ndisks: int, from_: str, aux: str, to: str):
        if ndisks == 0:
            return
        self.solve(ndisks - 1, from_, to, aux)
        self.move(from_, to)
        self.solve(ndisks - 1, aux, from_, to)


def solve(pegs: Pegs) -> int:
    pegs.solve(len(pegs["A"]), "A", "B", "C")
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
