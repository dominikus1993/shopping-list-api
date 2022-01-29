from typing import Any, Callable, Iterable
from typing import TypeVar
from typing import NewType

FoundIndex = NewType("Found", int)

T = TypeVar('T')

def find_index_by(sequence: Iterable[T], func: Callable[[T], Any]) -> FoundIndex | None:
    for index, item in enumerate(sequence):
        if func(item):
            return FoundIndex(index)
    return None