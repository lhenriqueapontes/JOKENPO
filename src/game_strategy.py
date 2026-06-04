import random
from collections import Counter

MOVES = ['rock', 'paper', 'scissors']
COUNTER = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
BEATS = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}


def choose_move(history):
    if not history:
        return random.choice(MOVES)
    opponent_moves = [x[1] for x in history]
    predicted = Counter(opponent_moves).most_common(1)[0][0]
    return COUNTER[predicted]


def round_score(a, b):
    if a == b:
        return 0
    if BEATS[a] == b:
        return 1
    return -1


def simulate(rounds=200):
    history = []
    score = 0
    for _ in range(rounds):
        a = choose_move(history)
        b = random.choice(MOVES)
        score += round_score(a, b)
        history.append((a, b))
    return {'rounds': rounds, 'score': score}


if __name__ == '__main__':
    print(simulate())
