from strategies.battle_strategy import BattleStrategy
from strategies.enemy_move import EnemyMove

class TacticalWaiting(BattleStrategy):
    def get_name(self) -> str:
        return self.__class__
    
    def get_counters(self) -> EnemyMove:
        return EnemyMove.TACTICAL_WAITING
    
    def perform(self):
        print(f"\nSoldiers waiting for orders! Patience is also a weapon!")