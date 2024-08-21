from abc import ABCMeta, abstractmethod
from strategies.enemy_move import EnemyMove

class BattleStrategy:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_counters(self) -> EnemyMove:
        pass

    @abstractmethod
    def perform(self):
        pass