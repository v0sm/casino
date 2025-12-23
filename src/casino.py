from src.player import Player
from src.goose import Goose
from src.chip import Chip
from src.player_collection import PlayerCollection
from src.goose_collection import GooseCollection
from src.chip_collection import ChipCollection
from src.casino_balance import CasinoBalance

import random


class Casino:
    def __init__(self) -> None:
        self.players = PlayerCollection()
        self.geese = GooseCollection()
        self.balances = CasinoBalance()
        self.chips_bank = ChipCollection()

        self._initialize_chip_bank()

    def _initialize_chip_bank(self) -> None:
        """Инициализировать банк казино фишками"""
        for nominal in Chip.nominals:
            chips = [Chip(nominal) for _ in range(100)]
            self.chips_bank.add(chips)

        total = self.chips_bank.total_value()
        print(f"[CASINO] Bank was initialized: {len(self.chips_bank)} chips with bank of {total}$")

    def register_player(self, name: str, initial_balance: int) -> Player:
        """Зарегистрировать нового игрока в казино"""
        player = Player(name, initial_balance)
        self.players.add(player)
        self.balances[player.name] = initial_balance

        print(f"[CASINO] Ludoman {name} will bring {initial_balance}$ earnings for casino")
        return player

    def register_goose(self, goose: Goose) -> None:
        """Зарегистрировать нового гуся в казино"""
        self.geese.add(goose)
        print(f"[CASINO] Goose {goose.name} ({type(goose).__name__}) is out for the hunt")

    def war_goose_attacks(self) -> None:
        """WarGoose атакует случайного игрока"""
        war_geese = self.geese.get_war_geese()

        if not war_geese or len(self.players) == 0:
            return

        goose = random.choice(war_geese)
        player = random.choice(self.players)

        try:
            stolen = goose.pluck(player)

            self.balances[player.name] = player.balance

            print(f"[EVENT] WarGoose {goose.name} plucked {stolen}$ from {player.name}'s pocket (balance: {player.balance}$)")
        except ValueError as e:
            print(f"[EVENT] WarGoose {goose.name} couldn't rob {player.name}: {e}")

    def honk_goose_honks(self) -> None:
        """HonkGoose гогочет и влияет на баланс случайного игрока"""
        honk_geese = self.geese.get_honk_geese()

        if not honk_geese or len(self.players) == 0:
            return

        goose = random.choice(honk_geese)
        player = random.choice(self.players)

        try:
            change = goose.honk(player)

            self.balances[player.name] = player.balance

            sign = "+" if change > 0 else ""
            print(f"[EVENT] HonkGoose {goose.name} honks! {player.name} {sign}{change}$ (balance: {player.balance}$)")
        except ValueError as e:
            print(f"[EVENT] HonkGoose {goose.name} tried to honk on {player.name}: {e}")

    def player_wins(self) -> None:
        """Случайный игрок выигрывает деньги"""
        if len(self.players) == 0:
            return

        player = random.choice(self.players)
        winnings = random.randint(10, 100)

        player.change_balance(winnings)
        self.balances[player.name] = player.balance

        print(f"[EVENT] {player.name} somehow won {winnings}$! Balance: {player.balance}$")

    def player_loses(self) -> None:
        """Случайный игрок проигрывает деньги"""
        if len(self.players) == 0:
            return

        player = random.choice(self.players)
        loss = random.randint(5, 50)

        actual_loss = min(loss, player.balance)

        if actual_loss == 0:
            print(f"[EVENT] {player.name} was about to lose but... He is broke already")
            return

        try:
            player.change_balance(-actual_loss)
            self.balances[player.name] = player.balance

            print(f"[EVENT] {player.name} lost {actual_loss}$. Balance: {player.balance}$")
        except ValueError as e:
            print(f"[EVENT] {player.name} couldn't lose: {e}")

    def player_places_bet(self) -> None:
        """Игрок делает ставку"""
        if len(self.players) == 0:
            return

        player = random.choice(self.players)

        if player.balance == 0:
            print(f"[EVENT] {player.name} wanted to place bet, but he can't bring any more profit for casino")
            return

        bet = random.randint(5, min(50, player.balance))

        try:
            player.place_bet(bet)
            self.balances[player.name] = player.balance

            print(f"[EVENT] {player.name} placed {bet}$. Remain: {player.balance}$")
        except ValueError as e:
            print(f"[EVENT] {player.name} couldn't place bet: {e}")

    def player_exchanges_chips(self) -> None:
        """Игрок обменивает деньги на фишки из банка казино"""
        if len(self.players) == 0:
            return

        player = random.choice(self.players)

        if player.balance == 0:
            print(f"[EVENT] {player.name} хотел обменять деньги, но у него 0$")
            return

        amount = random.randint(1, min(100, player.balance))

        try:
            chips_to_give = self._extract_chips_from_bank(amount)

            player.chips.add(chips_to_give)

            player.change_balance(-amount)
            self.balances[player.name] = player.balance

            print(f"[EVENT] {player.name} обменял {amount}$ на {len(chips_to_give)} фишек. Баланс: {player.balance}$")
        except ValueError as e:
            print(f"[EVENT] {player.name} не смог обменять деньги: {e}")

    def _extract_chips_from_bank(self, amount: int) -> list[Chip]:
        """Извлечь фишки из банка казино жадным алгоритмом.

        Args:
            amount: Сумма для обмена

        Returns:
            Список извлеченных фишек из банка

        Raises:
            ValueError: Если в банке недостаточно фишек для обмена
        """
        if self.chips_bank.total_value() < amount:
            raise ValueError("Недостаточно фишек в банке")

        extracted_chips = []
        remaining = amount

        for nominal in Chip.nominals:
            if remaining == 0:
                break

            indices_to_remove = []

            for i in range(len(self.chips_bank)):
                if remaining == 0:
                    break

                chip = self.chips_bank[i]

                if chip.value == nominal and chip.value <= remaining:
                    extracted_chips.append(chip)
                    indices_to_remove.append(i)
                    remaining -= chip.value

            for i in reversed(indices_to_remove):
                self.chips_bank.remove(i)

        if remaining > 0:
            self.chips_bank.add(extracted_chips)
            raise ValueError(f"Не удалось собрать точную сумму {amount}$")

        return extracted_chips

    def step(self) -> None:
        """Выполнить одно случайное событие"""
        events = [
            self.war_goose_attacks,
            self.honk_goose_honks,
            self.player_wins,
            self.player_loses,
            self.player_places_bet,
            self.player_exchanges_chips
        ]

        event = random.choice(events)
        event()

    def get_active_players(self) -> list:
        """Получить список игроков с балансом > 0"""
        return [p for p in self.players if self.balances[p.name] > 0]
