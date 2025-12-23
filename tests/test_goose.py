"""Тесты для классов гусей."""

import pytest
from src.goose import Goose, WarGoose, HonkGoose
from src.player import Player


class TestGoose:
    """Тесты базового гуся."""

    def test_goose_creation(self):
        """Тест создания базового гуся."""
        goose = Goose("TestGoose")
        assert goose.name == "TestGoose"


class TestWarGoose:
    """Тесты WarGoose."""

    def test_war_goose_creation(self):
        """Тест создания WarGoose."""
        goose = WarGoose("Bandit")
        assert goose.name == "Bandit"

    def test_war_goose_pluck_success(self):
        """Тест успешной кражи у игрока."""
        player = Player("Victim", 100)
        goose = WarGoose("Thief")

        stolen = goose.pluck(player)

        assert 1 <= stolen <= 50
        assert player.balance == 100 - stolen

    def test_war_goose_pluck_broke_player(self):
        """Тест кражи у разорившегося игрока."""
        player = Player("Broke", 0)
        goose = WarGoose("Thief")

        with pytest.raises(ValueError, match="There is nothing to pluck out"):
            goose.pluck(player)

    def test_war_goose_pluck_max_amount(self):
        """Тест, что украденная сумма не превышает баланс."""
        player = Player("SmallBalance", 10)
        goose = WarGoose("Thief")

        stolen = goose.pluck(player)

        assert stolen <= 10
        assert player.balance >= 0


class TestHonkGoose:
    """Тесты HonkGoose."""

    def test_honk_goose_creation(self):
        """Тест создания HonkGoose."""
        goose = HonkGoose("Honker", honk_volume=20)
        assert goose.name == "Honker"
        assert goose.honk_volume == 20

    def test_honk_goose_positive_honk(self):
        """Тест положительного гогота."""
        player = Player("Lucky", 100)
        goose = HonkGoose("Honker", honk_volume=30)

        change = goose.honk(player)

        assert -30 <= change <= 30
        assert player.balance == 100 + change

    def test_honk_goose_cannot_make_negative_balance(self):
        """Тест, что гогот не уводит баланс в минус."""
        player = Player("Poor", 5)
        goose = HonkGoose("Honker", honk_volume=50)

        change = goose.honk(player)

        assert player.balance >= 0
        assert change >= -5
