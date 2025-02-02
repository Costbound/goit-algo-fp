import random
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def simulate_dice_rolls(num_rolls):
    sums = [0] * 13  # Initialize a list to count sums from 2 to 12
    for _ in range(num_rolls):
        die1, die2 = roll_dice()
        sums[die1 + die2] += 1
    return sums

def calculate_probabilities(sums, num_rolls):
    probabilities = [count / num_rolls for count in sums]
    return probabilities

def plot_probabilities(probabilities, analytical_probabilities):
    sums = list(range(2, 13))
    plt.figure(figsize=(10, 6))
    plt.bar(sums, [p * 100 for p in probabilities[2:]], alpha=0.6, label='Monte Carlo')
    plt.plot(sums, [p * 100 for p in analytical_probabilities[2:]], 'ro-', label='Analytical')
    plt.xlabel('Sum of Two Dice')
    plt.ylabel('Probability (%)')
    plt.title('Probability of Sums of Two Dice Rolls')
    plt.legend()
    plt.grid(True)
    plt.show()

# Analytical probabilities for sums of two dice
analytical_probabilities = [0, 0, 1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]

# Number of simulations
num_rolls = 100000

# Simulate dice rolls
sums = simulate_dice_rolls(num_rolls)

# Calculate probabilities
probabilities = calculate_probabilities(sums, num_rolls)

# Print results in percentages
print("Sum\tMonte Carlo Probability \tAnalytical Probability")
for sum_value in range(2, 13):
    print(f"{sum_value}\t\t{probabilities[sum_value] * 100:.2f} %\t\t\t\t\t{analytical_probabilities[sum_value] * 100:.2f} %")

# Plot probabilities
plot_probabilities(probabilities, analytical_probabilities)