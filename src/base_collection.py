from typing import Generic, TypeVar, Iterator, Union

T = TypeVar('T')

class BaseCollection(Generic[T]):
    def __init__(self) -> None:
        self._items = []

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __getitem__(self, index: Union[int, slice]) -> Union[T, list[T]]:
        return self._items[index]

    def add(self, item: Union[T, list[T]]) -> None:
        if isinstance(item, list):
            self._items.extend(item)
        else:
            self._items.append(item)

    def remove(self, index: int) -> None:
        del self._items[index]
