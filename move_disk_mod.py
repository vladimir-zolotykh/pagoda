#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


Peg = list[int]
NDISKS = 3
from_: Peg = [*range(NDISKS, 0, -1)]
to: Peg = []
aux: Peg = []


def _move(from_: Peg, to: Peg) -> None:
    to.append(from_.pop())


def solve3():
    """
    >>> solve3()
    >>> from_
    []
    >>> to
    [3, 2, 1]
    >>> aux
    []
    >>>
    """
    ndisks = 3
    from_[:] = [*range(ndisks, 0, -1)]
    to[:] = []
    aux[:] = []

    _move(from_, to)
    _move(from_, aux)
    _move(to, aux)
    _move(from_, to)
    _move(aux, from_)
    _move(aux, to)
    _move(from_, to)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
