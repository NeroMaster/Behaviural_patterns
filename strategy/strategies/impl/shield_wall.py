from strategies.battle_strategy import BattleStrategy
from strategies.enemy_move import EnemyMove

class ShieldWall(BattleStrategy):
    def get_name(self) -> str:
        return self.__class__
    
    def get_counters(self) -> EnemyMove:
        return EnemyMove.ARROW_VALLEY
    
    def perform(self):
        print(f"\nSoldiers form shield wall to protect from arrow valley!")