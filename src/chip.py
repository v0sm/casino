from __future__ import annotations

class Chip:
    nominals = [1000, 500, 250, 100, 50, 25, 10, 5, 1]

    def __init__(self, value: int) -> None:
        self.value = value

    def __add__(self, other_chip: Chip) -> Chip:
        chip_2 = Chip(self.value + other_chip.value)
        return chip_2

    @staticmethod
    def exchange(amount: int) -> list[Chip]:
        chips = []
        remaining = amount
        for nominal in Chip.nominals:
            count = remaining // nominal
            if count > 0:
                for i in range(count):
                    chip = Chip(nominal)
                    chips.append(chip)
                remaining -= nominal * count
            if remaining == 0:
                break
        return chips
