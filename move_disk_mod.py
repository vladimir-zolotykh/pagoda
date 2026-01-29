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
    >>> from_peg[:] = [2, 1]
    >>> to_peg[:] = []
    >>> aux_peg[:] = []
    >>> solve(2)
    >>> from_peg
    []
    >>> aux_peg
    []
    >>> to_peg
    [2, 1]
    """
    if ndisks == 1:
        _move(from_, to)
    elif ndisks == 2:
        _move(from_, aux)
        _move(from_, to)
        _move(aux, to)
    else:
        raise NotImplementedError(f"Don't know how to move {ndisks} disks")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
