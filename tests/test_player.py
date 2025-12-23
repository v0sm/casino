"""Тесты для класса Player."""

import pytest
from src.player import Player
from src.chip import Chip


class TestPlayer:
    """Тесты игрока."""

    def test_player_creation(self):
        """Тест создания игрока с валидными параметрами."""
        player = Player("Alice", 100)
        assert player.name == "Alice"
        assert player.balance == 100
        assert len(player.chips) == 0

    def test_player_negative_balance_raises(self):
        """Тест, что отрицательный баланс вызывает исключение."""
        with pytest.raises(ValueError, match="You can't play in this casino!"):
            Player("Bob", -10)

    def test_change_balance_positive(self):
        """Тест увеличения баланса."""
        player = Player("Alice", 100)
        player.change_balance(50)
        assert player.balance == 150

    def test_change_balance_negative(self):
        """Тест уменьшения баланса."""
        player = Player("Alice", 100)
        player.change_balance(-30)
        assert player.balance == 70

    def test_change_balance_to_negative_raises(self):
        """Тест, что попытка уйти в минус вызывает исключение."""
        player = Player("Alice", 50)
        with pytest.raises(ValueError, match="You are broke!"):
            player.change_balance(-100)

    def test_place_bet_valid(self):
        """Тест успешной ставки."""
        player = Player("Alice", 100)
        bet = player.place_bet(25)
        assert bet == 25
        assert player.balance == 75

    def test_place_bet_exceeds_balance(self):
        """Тест, что ставка больше баланса вызывает исключение."""
        player = Player("Alice", 50)
        with pytest.raises(ValueError, match="Your bet is too high for your balance!"):
            player.place_bet(100)

    def test_place_bet_zero(self):
        """Тест, что нулевая или отрицательная ставка работает корректно."""
        player = Player("Alice", 100)
        bet = player.place_bet(10)
        assert bet == 10

    def test_player_with_chips(self):
        """Тест добавления фишек игроку."""
        player = Player("Alice", 100)
        chips = [Chip(5), Chip(10), Chip(25)]
        player.chips.add(chips)
        assert len(player.chips) == 3
        assert player.chips.total_value() == 40
