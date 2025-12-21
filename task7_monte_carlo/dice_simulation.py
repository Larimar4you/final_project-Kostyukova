import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    """
    Симуляція кидків двох кубиків методом Монте-Карло
    та обчислення ймовірностей сум.
    """
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        sums_count[total] += 1

    probabilities = {total: count / num_rolls for total, count in sums_count.items()}

    return probabilities


def plot_probabilities(probabilities, num_rolls):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(8, 5))
    plt.bar(sums, probs)
    plt.xlabel("Сума чисел на кубиках")
    plt.ylabel("Ймовірність")
    plt.title(f"Метод Монте-Карло ({num_rolls} кидків)")
    plt.grid(axis="y")

    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha="center", va="bottom")

    plt.show()


if __name__ == "__main__":
    # Різна кількість симуляцій для демонстрації збіжності
    for accuracy in [100, 1000, 10000, 100000]:
        probabilities = simulate_dice_rolls(accuracy)

        print(f"\nКількість кидків: {accuracy}")
        print(f"{'Сума':<5}{'Ймовірність'}")
        for s in range(2, 13):
            print(f"{s:<5}{probabilities[s]:.4f}")

        plot_probabilities(probabilities, accuracy)
