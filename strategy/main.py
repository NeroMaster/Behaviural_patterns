from strategies.enemy_move import EnemyMove
from general import General

BLOCK_DELIMITER = "\n--\n"

def main():
    general = General()
    general.act(EnemyMove.ARROW_VALLEY)
    print(BLOCK_DELIMITER)

    general.act(EnemyMove.HORSEMAN_ATTACK)
    print(BLOCK_DELIMITER)

    general.act(EnemyMove.TACTICAL_WAITING)
    print(BLOCK_DELIMITER)

if __name__ == "__main__":
    main()