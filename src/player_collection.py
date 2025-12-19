from typing import Union

from src.base_collection import BaseCollection
from src.player import Player


class PlayerCollection(BaseCollection[Player]):
    def get_by_name(self, name: str) -> Union[Player, None]:
        for player in self._items:
            if player.name == name:
                return player
        return None
