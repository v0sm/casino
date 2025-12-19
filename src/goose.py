from src.player import Player
import random

class Goose:
    def __init__(self, name: str, honk_volume: int = 1):
        if honk_volume <= 0:
            raise ValueError("This Goose can't be real")
        if honk_volume > 100:
            raise ValueError("This Goose is too loud")
        self.name = name
        self.honk_volume = honk_volume

class WarGoose(Goose):
    @staticmethod
    def pluck(player:Player) -> int:
        if player.balance == 0:
            raise ValueError("There is nothing to pluck out")
        max_steal = max(1, player.balance // 2)
        amount = random.randint(1, max_steal)
        player.change_balance(-amount)
        return amount

class HonkGoose(Goose):
    def honk(self, player: Player) -> int:
        max_amount = max(1, player.balance * self.honk_volume // 100)
        condition = random.randint(0, 1)
        if condition == 0:
            if player.balance == 0:
                raise ValueError("Player is broke, honking is meaningless")
            amount = -random.randint(1, max_amount)
            player.change_balance(amount)
            return amount
        else:
            amount = random.randint(1, max_amount)
            player.change_balance(amount)
            return amount
