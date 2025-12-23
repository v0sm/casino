"""Тесты для Casino и симуляции."""

import pytest
import random
from src.casino import Casino
from src.goose import WarGoose, HonkGoose
from src.simulation import run_simulation


class TestCasino:
    """Тесты казино."""

    def test_casino_creation(self):
        """Тест создания казино."""
        casino = Casino()
        assert len(casino.players) == 0
        assert len(casino.geese) == 0
        assert casino.chips_bank.total_value() > 0

    def test_register_player(self):
        """Тест регистрации игрока."""
        casino = Casino()
        player = casino.register_player("Alice", 150)

        assert player.name == "Alice"
        assert player.balance == 150
        assert len(casino.players) == 1
        assert casino.balances["Alice"] == 150

    def test_register_goose(self):
        """Тест регистрации гуся."""
        casino = Casino()
        goose = WarGoose("Thief")
        casino.register_goose(goose)

        assert len(casino.geese) == 1
        assert casino.geese[0] == goose

    def test_step_executes(self):
        """Тест, что шаг симуляции выполняется без ошибок."""
        random.seed(42)
        casino = Casino()
        casino.register_player("Alice", 100)
        casino.register_goose(WarGoose("Goose1"))

        casino.step()

        assert len(casino.players) >= 0

    def test_get_active_players(self):
        """Тест получения активных игроков."""
        casino = Casino()
        casino.register_player("Alice", 100)
        casino.register_player("Bob", 0)

        active = casino.get_active_players()
        assert len(active) == 1
        assert active[0].name == "Alice"


class TestSimulation:
    """Тесты симуляции."""

    def test_run_simulation_completes(self, capsys):
        """Тест, что симуляция завершается без ошибок."""
        run_simulation(steps=5, seed=999)

        captured = capsys.readouterr()
        assert "CASINO" in captured.out
        assert "Bank was initialized" in captured.out

    def test_simulation_reproducible(self, capsys):
        """Тест воспроизводимости симуляции с одинаковым seed."""
        run_simulation(steps=3, seed=123)
        output1 = capsys.readouterr().out

        run_simulation(steps=3, seed=123)
        output2 = capsys.readouterr().out

        assert output1 == output2
