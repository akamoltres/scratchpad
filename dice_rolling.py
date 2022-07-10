# Roll a d20. Let's say you roll a 13. Then roll a d13.
# Let's say you roll a 5. The roll a d5. Continue this
# process until you roll a 1. What is the expected number
# of dice rolls you make, starting with the d20 roll?

import argparse
from math import ceil
import random

PLT_WIDTH = 20

def plot(labels, values):
    max_val = max(values)
    ratios = [v / max_val for v in values]
    widths = [ceil(r * PLT_WIDTH) for r in ratios]
    print("Rolls\tInstances")
    for i,w in enumerate(widths):
        print(f"{labels[i]}\t{'#'*w} {values[i]}")

    weighted = [(i + 1) * values[i] for i in range(len(values))]
    weighted_avg = sum(weighted) / sum(values)
    print(f"Expected number of rolls: {weighted_avg}")

def main(_die):
    move_dist = dict()
    for iteration in range(100000):
        moves = 0
        die = _die
        while die != 1:
            die = random.randint(1, die)
            moves += 1
        if moves in move_dist.keys():
            move_dist[moves] += 1
        else:
            move_dist[moves] = 1

    move_labels = [f"{str(i)}" for i in range(1, max(move_dist.keys()) + 1)]
    move_list = [0] * (max(move_dist.keys()))
    for moves in move_dist.keys():
        move_list[moves - 1] = move_dist[moves]

    plot(move_labels, move_list)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("die", help="Number of sides on the die", type=int)
    parser.add_argument("--seed", help="RNG seed (default 12)", type=int, default=12)
    args = parser.parse_args()
    random.seed(args.seed)
    main(args.die)
