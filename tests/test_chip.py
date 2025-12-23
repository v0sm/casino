"""Тесты для класса Chip."""

import pytest
from src.chip import Chip


class TestChip:
    """Тесты фишек."""

    def test_chip_creation(self):
        """Тест создания фишки с валидным номиналом."""
        chip = Chip(25)
        assert chip.value == 25

    def test_chip_creation_all_nominals(self):
        """Тест создания фишек всех номиналов."""
        for nominal in Chip.nominals:
            chip = Chip(nominal)
            assert chip.value == nominal

    def test_chip_nominals(self):
        """Тест списка доступных номиналов."""
        expected = [1000, 500, 250, 100, 50, 25, 10, 5, 1]
        assert Chip.nominals == expected

    def test_chip_exchange_exact_amount(self):
        """Тест обмена точной суммы."""
        chips = Chip.exchange(136)
        values = [c.value for c in chips]

        assert sum(values) == 136
        assert 100 in values
        assert 25 in values
        assert 10 in values
        assert 1 in values

    def test_chip_exchange_small_amount(self):
        """Тест обмена маленькой суммы."""
        chips = Chip.exchange(7)
        assert sum(c.value for c in chips) == 7

    def test_chip_exchange_zero(self):
        """Тест, что обмен нуля возвращает пустой список."""
        chips = Chip.exchange(0)
        assert chips == []

    def test_chip_exchange_large_amount(self):
        """Тест обмена большой суммы."""
        chips = Chip.exchange(5000)
        assert sum(c.value for c in chips) == 5000
