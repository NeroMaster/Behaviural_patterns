from strategies.battle_strategy import BattleStrategy
from strategies.enemy_move import EnemyMove

class SpearmanDefence(BattleStrategy):
    def get_name(self) -> str:
        return self.__class__
    
    def get_counters(self) -> EnemyMove:
        return EnemyMove.HORSEMAN_ATTACK
    
    def perform(self):
        print(f"\nSoldiers move forward and lower their spears, preparing to take the attack of the enemy!")