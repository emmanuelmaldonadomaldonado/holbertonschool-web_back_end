#!/usr/bin/env python3
''' Description: Annotate the below function’s parameters and
                 return values with the appropriate types
    Arguments: lst: Iterable[Sequence]
'''

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
