"""Тесты для коллекций."""

import pytest
from src.player import Player
from src.player_collection import PlayerCollection
from src.goose import WarGoose, HonkGoose
from src.goose_collection import GooseCollection
from src.chip import Chip
from src.chip_collection import ChipCollection


class TestPlayerCollection:
    """Тесты коллекции игроков."""

    def test_add_player(self):
        """Тест добавления игрока."""
        collection = PlayerCollection()
        player = Player("Alice", 100)
        collection.add(player)

        assert len(collection) == 1
        assert collection[0] == player

    def test_remove_player_by_index(self):
        """Тест удаления игрока по индексу."""
        collection = PlayerCollection()
        player = Player("Alice", 100)
        collection.add(player)
        collection.remove(0)

        assert len(collection) == 0

    def test_iteration(self):
        """Тест итерации по коллекции."""
        collection = PlayerCollection()
        players = [Player(f"Player{i}", 100) for i in range(3)]

        for player in players:
            collection.add(player)

        assert len(list(collection)) == 3


class TestGooseCollection:
    """Тесты коллекции гусей."""

    def test_get_war_geese(self):
        """Тест получения только WarGoose."""
        collection = GooseCollection()
        war1 = WarGoose("War1")
        war2 = WarGoose("War2")
        honk = HonkGoose("Honk1", 10)

        collection.add(war1)
        collection.add(war2)
        collection.add(honk)

        war_geese = collection.get_war_geese()
        assert len(war_geese) == 2
        assert all(isinstance(g, WarGoose) for g in war_geese)

    def test_get_honk_geese(self):
        """Тест получения только HonkGoose."""
        collection = GooseCollection()
        war = WarGoose("War1")
        honk1 = HonkGoose("Honk1", 10)
        honk2 = HonkGoose("Honk2", 20)

        collection.add(war)
        collection.add(honk1)
        collection.add(honk2)

        honk_geese = collection.get_honk_geese()
        assert len(honk_geese) == 2
        assert all(isinstance(g, HonkGoose) for g in honk_geese)


class TestChipCollection:
    """Тесты коллекции фишек."""

    def test_total_value(self):
        """Тест подсчета общей стоимости фишек."""
        collection = ChipCollection()
        chips = [Chip(100), Chip(50), Chip(25)]
        collection.add(chips)

        assert collection.total_value() == 175

    def test_empty_collection_value(self):
        """Тест, что пустая коллекция имеет нулевую стоимость."""
        collection = ChipCollection()
        assert collection.total_value() == 0
