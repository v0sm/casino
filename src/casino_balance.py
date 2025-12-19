from typing import Iterator

class CasinoBalance:
    def __init__(self) -> None:
        self._data = {}

    def __getitem__(self, key: str) -> int:
        return self._data[key]

    def __setitem__(self, key: str, value: int) -> None:
        if key in self._data:
            old = self._data[key]
            print(f"[BALANCE] {key}: {old} -> {value}")
        else:
            print(f"[BALANCE] New player {key}, balance: {value}")

        self._data[key] = value

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator[str]:
        return iter(self._data)
