from src.base_collection import BaseCollection
from src.goose import Goose, WarGoose, HonkGoose


class GooseCollection(BaseCollection[Goose]):
    def get_war_geese(self) -> list[WarGoose]:
        return [goose for goose in self._items if isinstance(goose, WarGoose)]

    def get_honk_geese(self):
        return [goose for goose in self._items if isinstance(goose, HonkGoose)]
