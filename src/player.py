from src.chip_collection import ChipCollection

class Player:
    def __init__(self, name: str, balance: int = 0) -> None:
        if balance < 0:
            raise ValueError("You can't play in this casino!")
        self.balance = balance
        self.name = name
        self.chips = ChipCollection()

    def change_balance(self, amount: int) -> None:
        if self.balance + amount < 0:
            raise ValueError("You are broke!")
        self.balance += amount

    def place_bet(self, amount: int) -> int:
        if self.balance < amount:
            raise ValueError("Your bet is too high for your balance!")
        self.balance -= amount
        return amount
