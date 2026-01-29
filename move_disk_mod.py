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


def solve1():
    """
    >>> solve1()
    >>> to
    [1]
    """
    from_[:] = [1]
    to[:] = []
    aux[:] = []

    _move(from_, to)


def solve2():
    """
    >>> solve2()
    >>> from_
    []
    >>> aux
    []
    >>> to
    [2, 1]
    """
    from_[:] = [2, 1]
    to[:] = []
    aux[:] = []

    _move(from_, aux)
    _move(from_, to)
    _move(aux, to)


def solve3_2():
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
    solve2()
    _move(from_, aux)
    _move(to, aux)
    _move(to, from_)
    _move(aux, from_)
    _move(aux, to)
    solve2()


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

    for tup in (
        (from_, to),
        (from_, aux),
        (to, aux),
        (from_, to),
        (aux, from_),
        (aux, to),
        (from_, to),
    ):
        _move(tup[0], tup[1])


def solve4():
    """
    >>> solve4()
    >>> from_
    []
    >>> to
    [4, 3, 2, 1]
    >>> aux
    []
    >>>
    """
    ndisks = 4
    from_[:] = [*range(ndisks, 0, -1)]
    to[:] = []
    aux[:] = []

    for tup in (
        (from_, aux),
        (from_, to),
        (aux, to),
        (from_, aux),
        (to, from_),
        (to, aux),
        (from_, aux),
        (from_, to),
        (aux, to),
        (aux, from_),
        (to, from_),
        (aux, to),
        (from_, aux),
        (from_, to),
        (aux, to),
    ):
        _move(tup[0], tup[1])


def solve5():
    """
    >>> solve5()
    >>> from_
    []
    >>> to
    [5, 4, 3, 2, 1]
    >>> aux
    []
    >>>
    """
    ndisks = 5
    from_[:] = [*range(ndisks, 0, -1)]
    to[:] = []
    aux[:] = []

    for tup in (
        (from_, to),
        (from_, aux),
        (to, aux),
        (from_, to),
        (aux, from_),
        (aux, to),
        (from_, to),
        (from_, aux),
        (to, aux),
        (to, from_),
        (aux, from_),
        (to, aux),
        (from_, to),
        (from_, aux),
        (to, aux),
        (from_, to),
        (aux, from_),
        (aux, to),
        (from_, to),
        (aux, from_),
        (to, aux),
        (to, from_),
        (aux, from_),
        (aux, to),
        (from_, to),
        (from_, aux),
        (to, aux),
        (from_, to),
        (aux, from_),
        (aux, to),
        (from_, to),
    ):
        _move(tup[0], tup[1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
