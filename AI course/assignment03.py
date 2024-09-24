import random
import math

class attackingGame:
    def __init__(self):
        self.hp = None

    def alphabeta(self, init_life, num_of_bullet, min_val, max_val, depth, alpha, beta, maximize):
        if (depth == 0 or init_life <= 0):
            return -init_life, None, 0

        prune = 0

        if maximize:
            hp = float('-inf')
            outcome = None

            for i in range(1, num_of_bullet + 1):
                damage = random.choice(range(min_val, max_val+1))
                outcome = damage

                hp = max(hp, self.alphabeta(init_life - damage, num_of_bullet, min_val, max_val, depth - 1, alpha, beta, False)[0])
                prune += self.alphabeta(init_life - damage, num_of_bullet, min_val, max_val, depth - 1, alpha, beta, False)[2]
                alpha = max(alpha, hp)

                if (beta <= alpha):
                    prune = prune + (num_of_bullet - i)
                    # print("=======================if===========================", prune)
                    break

            return hp, outcome, prune

        else:
            hp = float('inf')
            outcome = None

            for i in range(1, num_of_bullet + 1):
                damage = random.choice(range(min_val, max_val+1))
                outcome = None

                hp = min(hp, self.alphabeta(init_life - damage, num_of_bullet, min_val, max_val, depth - 1, alpha, beta, True)[0])
                prune += self.alphabeta(init_life - damage, num_of_bullet, min_val, max_val, depth - 1, alpha, beta, False)[2]
                beta = min(beta, hp)

                if (beta <= alpha):
                    prune = prune + (num_of_bullet - i)
                    # print("==================else============================", prune)
                    break

            return hp, outcome, prune

    def details(self):
        student_id = input("Enter your student id: ")
        min_max_range = input("Minimum and Maximum hp for the range of negative HP: ")
        turns, init_life, num_of_bullet = map(int, (student_id[0], student_id[-2:][::-1], student_id[2]))
        depth = 2 * turns
        branch = int(math.pow(num_of_bullet, depth))
        min_val, max_val = map(int, min_max_range.split())
        max_neg_hp, outcome, prune = self.alphabeta(init_life, num_of_bullet, min_val, max_val, depth, float('-inf'), float('inf'), True)
        left_life_hp = (init_life - (-max_neg_hp))
        t_nodes = [str(random.choice(range(min_val, max_val + 1))) for visit in range(branch)]
        terminal_nodes = ", ".join(t_nodes)


        ##################### printing lines #####################
        # print(turns)
        # print(init_life)
        # print(num_of_bullet)
        # print(depth)
        # print(max_neg_hp)
        # print(prune)
        print("Depth and Branches ratio is {0}:{1}".format(depth, num_of_bullet))
        print(f"Terminal States (leaf node values) are {terminal_nodes}")
        print(f"Left life(HP) of the defender after maximum damage caused by the attacker is {left_life_hp}")
        print(f"After Alpha-Beta Pruning Leaf Node Comparisons {branch-prune}")

attackingGameDriver = attackingGame()
attackingGameDriver.details()