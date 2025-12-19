items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    total_cost = 0
    total_calories = 0
    chosen_items = []

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            total_cost += data["cost"]
            total_calories += data["calories"]
            chosen_items.append(name)

    return chosen_items, total_cost, total_calories


def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = items[item_names[i - 1]]["cost"]
        calories = items[item_names[i - 1]]["calories"]

        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]

    chosen_items = []
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            chosen_items.append(item_names[i - 1])
            b -= items[item_names[i - 1]]["cost"]

    chosen_items.reverse()

    total_calories = dp[n][budget]
    total_cost = sum(items[item]["cost"] for item in chosen_items)

    return chosen_items, total_cost, total_calories


budget = 150

print("Greedy algorithm:")
result_greedy = greedy_algorithm(items, budget)
print(result_greedy)

print("\nDynamic programming:")
result_dp = dynamic_programming(items, budget)
print(result_dp)

"""
Greedy algorithm:
(['cola', 'potato', 'pepsi', 'hot-dog', 'hamburger'], 120, 1120)

Dynamic programming:
(['pizza', 'hamburger', 'pepsi', 'cola', 'potato'], 140, 1220)
"""
