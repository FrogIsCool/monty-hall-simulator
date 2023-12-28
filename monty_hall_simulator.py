import sys
import random
from datetime import datetime

def do_choose_iteration():
    result = [0, 0]

    doors = [0, 0, 0]
    random.seed(datetime.now().timestamp())
    door = random.randint(0, 2)
    doors[door] = 1

    chosen = random.randint(0, 2)
    result[0] = doors[chosen]

    if doors[chosen] == 1:
        result[1] = 0
    else:
        result[1] = 1

    return result


if len(sys.argv) != 2:
    print("Expected one argument for number of iterations to run\n")
    exit(1)

n = int(sys.argv[1])

stay_wins = 0
switch_wins = 0

for i in range(n):
    result = do_choose_iteration()
    stay_wins = stay_wins + result[0]
    switch_wins = switch_wins + result[1]

print("Outcome of simulation:\n")
print("Wins if no change:", stay_wins, "\n")
print("Wins if door choice is changed:", switch_wins, "\n")

