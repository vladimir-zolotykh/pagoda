#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


Peg = list[int]
NDISKS = 3
from_: Peg = [*range(NDISKS, 0, -1)]
to: Peg = []
aux: Peg = []


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

    to.append(from_.pop())
    aux.append(from_.pop())
    aux.append(to.pop())
    to.append(from_.pop())
    from_.append(aux.pop())
    to.append(aux.pop())
    to.append(from_.pop())


if __name__ == "__main__":
    import doctest

    doctest.testmod()
