from typing import Dict, List
from strategies.battle_strategy import BattleStrategy
from strategies.enemy_move import EnemyMove
from strategies.impl.shield_wall import ShieldWall
from strategies.impl.spearman_defence import SpearmanDefence
from strategies.impl.tactical_waiting import TacticalWaiting

class General:
    _strategies: Dict[str, BattleStrategy]

    def __init__(self) -> None:
        self._experience = [
            ShieldWall(),
            SpearmanDefence(),
            TacticalWaiting()
        ]
        self._strategies = {
            EnemyMove.ARROW_VALLEY.value: ShieldWall(),
            EnemyMove.HORSEMAN_ATTACK.value: SpearmanDefence(),
            EnemyMove.TACTICAL_WAITING.value: TacticalWaiting()
        }

    def act(self, move: EnemyMove):
        tactic: BattleStrategy = self._strategies.get(move.value)
        print(f"General select {tactic.get_name()} to counter {move.value}!")
        tactic.perform()