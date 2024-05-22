class Item:
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories
        self.ratio = calories / cost

def greedy_algorithm(items, budget):
    # Сортуємо предмети 
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for item in items:
        if total_cost + item.cost <= budget:
            selected_items.append(item.name)
            total_cost += item.cost
            total_calories += item.calories
    
    return selected_items, total_cost, total_calories


items = [
    Item("pizza", 50, 300),
    Item("hamburger", 40, 250),
    Item("hot-dog", 30, 200),
    Item("pepsi", 10, 100),
    Item("cola", 15, 220),
    Item("potato", 25, 350)
]


budget = 200


selected_items, total_cost, total_calories = greedy_algorithm(items, budget)

print("Selected Items:", selected_items)
print("Total Cost:", total_cost)
print("Total Calories:", total_calories)
