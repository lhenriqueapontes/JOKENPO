from pathlib import Path
import csv
import random
from strategy_bot import frequency_bot, markov_bot, result, MOVES


def random_player(history):
    return random.choice(MOVES)


def simulate(bot, rounds=300):
    history = []
    score = 0
    wins = draws = losses = 0
    for _ in range(rounds):
        a = bot(history)
        b = random_player(history)
        r = result(a, b)
        score += r
        if r == 1:
            wins += 1
        elif r == 0:
            draws += 1
        else:
            losses += 1
        history.append((a, b))
    return {'rounds': rounds, 'score': score, 'wins': wins, 'draws': draws, 'losses': losses}


def main():
    Path('reports').mkdir(exist_ok=True)
    rows = [
        {'strategy': 'frequency_bot', **simulate(frequency_bot)},
        {'strategy': 'markov_bot', **simulate(markov_bot)},
    ]
    with open('reports/strategy_results.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(rows)


if __name__ == '__main__':
    main()
