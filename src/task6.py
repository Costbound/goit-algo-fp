items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Sort items by calories-to-cost ratio in descending order
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']

    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item, info = item_list[i - 1]
        cost = info['cost']
        calories = info['calories']
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    total_calories = dp[n][budget]
    total_cost = 0
    selected_items = []
    w = budget

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item, info = item_list[i - 1]
            selected_items.append(item)
            total_cost += info['cost']
            w -= info['cost']

    selected_items.reverse()
    return selected_items, total_cost, total_calories

# Example usage
budget = 100

# Greedy algorithm
greedy_selected_items, greedy_total_cost, greedy_total_calories = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Selected items:", greedy_selected_items)
print("Total cost:", greedy_total_cost)
print("Total calories:", greedy_total_calories)

# Dynamic programming
dp_selected_items, dp_total_cost, dp_total_calories = dynamic_programming(items, budget)
print("\nDynamic Programming:")
print("Selected items:", dp_selected_items)
print("Total cost:", dp_total_cost)
print("Total calories:", dp_total_calories)