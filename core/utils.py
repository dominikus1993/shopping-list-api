from typing import Any, Callable, Iterable
from typing import TypeVar


T = TypeVar('T')
def find_index_by(sequence: Iterable[T], func: Callable[[T], Any]) -> int:
    for index, item in enumerate(sequence):
        if func(item):
            return index
    return -1