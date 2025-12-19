from src.base_collection import BaseCollection
from src.chip import Chip

class ChipCollection(BaseCollection[Chip]):
    def total_value(self) -> int:
        return sum(chip.value for chip in self._items)

    def add_chips_from_exchange(self, amount: int) -> None:
        chips = Chip.exchange(amount)
        self.add(chips)

    def clear(self) -> None:
        self._items.clear()

    def pop(self, index: int = -1) -> Chip:
        return self._items.pop(index)

    def __repr__(self) -> str:
        if not self._items:
            return "ChipCollection(пусто)"

        counts = {}
        for chip in self._items:
            counts[chip.value] = counts.get(chip.value, 0) + 1

        parts = [f"{count}x{value}$" for value, count in sorted(counts.items(), reverse=True)]
        return f"ChipCollection({', '.join(parts)})"
