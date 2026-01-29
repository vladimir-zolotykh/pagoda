#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


PegType = list[int]
from_peg: PegType = []
to_peg: PegType = []
aux_peg: PegType = []


def _move(from_: PegType, to: PegType) -> None:
    to.append(from_.pop())


def solve(
    ndisks: int, from_: PegType = from_peg, to: PegType = to_peg, aux: PegType = aux_peg
) -> None:
    """
    >>> from_peg[:] = [1]
    >>> solve(1)
    >>> from_peg
    []
    >>> aux_peg
    []
    >>> to_peg
    [1]
    """
    if ndisks == 1:
        _move(from_, to)
    else:
        raise NotImplementedError(f"Don't know how to move {ndisks} disks")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
