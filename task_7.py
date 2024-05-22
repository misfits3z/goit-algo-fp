
import random

def throw_dice():
    return random.randint(1, 6) + random.randint(1, 6)
sum_freq = {i: 0 for i in range(2, 13)}

num_simulations = 10000

for _ in range(num_simulations):
    dice_sum = throw_dice()
    sum_freq[dice_sum] += 1

probabilities = {key: value / num_simulations for key, value in sum_freq.items()}

for key, value in probabilities.items():
    print(f"Cума: {key}, Ймовірність: {value}")



