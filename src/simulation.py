from src.casino import Casino
from src.goose import WarGoose, HonkGoose

import random

def run_simulation(steps: int = 20, seed: int = None) -> None:
    """Запустить симуляцию казино

    Args:
        steps: количество шагов симуляции
        seed: seed для генератора случайных чисел (для воспроизводимости)
    """
    if seed is not None:
        random.seed(seed)

    casino = Casino()

    print("РЕГИСТРАЦИЯ УЧАСТНИКОВ")

    casino.register_player("Вася", 100)
    casino.register_player("Петя", 150)
    casino.register_player("Коля", 80)

    casino.register_goose(WarGoose(name="Гога"))
    casino.register_goose(WarGoose(name="Гриша"))
    casino.register_goose(HonkGoose(name="Жора", honk_volume=10))

    print(f"\nНАЧАЛО СИМУЛЯЦИИ ({steps} шагов, seed={seed})")

    for i in range(1, steps + 1):
        print(f"Шаг {i}")
        casino.step()
        print()
