#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from dataclasses import dataclass, field


@dataclass
class Pegs:
    """
    pegs = Pegs(3)
    """

    ndisks: int
    from_: list[int] = field(init=False)
    aux: list[int] = field(init=False)
    to: list[int] = field(init=False)

    def __post_init__(self):
        self.from_ = list(range(self.ndisks, 0, -1))
        self.aux = []
        self.to = []

    @property
    def src_disks(self) -> int:
        return len(self.from_)


NDISKS = 4


def init_pegs(ndisks=NDISKS) -> Pegs:
    pegs = Pegs(ndisks)
    return pegs


def move(pegs: Pegs, from_: int, to: int) -> Pegs:
    d = pegs.from_.pop()
    pegs.append(d)
    return pegs


def solve(pegs: Pegs) -> Pegs:
    """
    A - smallest disk, pegs: 1 (source), 2 (auxiliary), 3 (target)
    move("A", 1, 3)
    move("B", 1, 2)
    move("A", 3, 2)
    move("C", 1, 3)
    move("A", 2, 1)
    move("B", 2, 3)
    move("A", 1, 3)
    """
    pass


if __name__ == "__main__":
    pegs = Pegs(4)
    pegs = solve(pegs)
    print(pegs)
