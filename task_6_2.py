def dynamic_programming(budget, items):
    costs = [item["cost"] for item in items.values()]
    calories = [item["calories"] for item in items.values()]

    n = len(costs)
    K = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                K[i][w] = max(calories[i - 1] + K[i - 1][w - costs[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][budget]

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 200

max_calories = dynamic_programming(budget, items)
print("Maximum calories:", max_calories)
