from typing import Generic, TypeVar, Iterator, Union, Optional

T = TypeVar('T')

class BaseCollection(Generic[T]):
    def __init__(self, items: Optional[list[T]] = None) -> None:
        self._items = items if items is not None else []

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __getitem__(self, index: Union[int, slice]) -> Union[T, list[T]]:
        if isinstance(index, slice):
            return self.__class__(self._items[index])
        elif isinstance(index, int):
            return self._items[index]
        raise TypeError("Index must be int or slice")

    def add(self, item: Union[T, list[T]]) -> None:
        if isinstance(item, list):
            self._items.extend(item)
        else:
            self._items.append(item)

    def remove(self, index: int) -> None:
        del self._items[index]
