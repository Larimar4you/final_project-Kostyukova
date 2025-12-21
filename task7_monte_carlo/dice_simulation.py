import random
from collections import Counter

import matplotlib.pyplot as plt


def monte_carlo_dice_simulation(num_trials=100000):
    sums = []

    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sums.append(dice1 + dice2)

    counts = Counter(sums)

    probabilities = {total: counts.get(total, 0) / num_trials for total in range(2, 13)}

    return probabilities


# Запуск
trials = 100_000
mc_probabilities = monte_carlo_dice_simulation(trials)

analytical_probabilities = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}

sums = list(mc_probabilities.keys())
mc_values = list(mc_probabilities.values())
an_values = [analytical_probabilities[s] for s in sums]

plt.bar(sums, mc_values, alpha=0.6, label="Monte Carlo")
plt.plot(sums, an_values, marker="o", color="red", label="Analytical")

plt.xlabel("Sum of dice")
plt.ylabel("Probability")
plt.title("Monte Carlo vs Analytical Probabilities")
plt.legend()
plt.grid(True)
plt.show()

# Вивід
print(f"{'Sum':<5}{'Monte Carlo':<15}{'Analytical'}")
for s in range(2, 13):
    print(f"{s:<5}{mc_probabilities[s]:<15.4f}{analytical_probabilities[s]:.4f}")

"""
Sum  Monte Carlo    Analytical
2    0.0268         0.0278
3    0.0545         0.0556
4    0.0841         0.0833
5    0.1123         0.1111
6    0.1403         0.1389
7    0.1656         0.1667
8    0.1402         0.1389
9    0.1115         0.1111
10   0.0818         0.0833
11   0.0551         0.0556
12   0.0278         0.0278
"""
