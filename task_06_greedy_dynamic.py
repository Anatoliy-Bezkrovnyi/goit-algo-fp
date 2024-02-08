

def greedy_calories(budget, menu):
    your_meal = {} # Словник із найбільш калорійних страв та напоїв із цінами
    meals_ratio = {} # Словник із розрахунком кількості калорій яку можна купити за гривню, від найбільш до найменш вигідного придбання 
    total_calories = 0 # Підрахунок калорійності обіду
    
    # Розрахунком кількості калорій яку можна купити за гривню
    for meal, details in menu.items():
        ratio = details["calories"] /  details["cost"] #
        meals_ratio[meal] = ratio    
    
    # Сортування отриманого словника від найбільш до найменш вигідного придбання
    sorted_meals_ratio = dict(sorted(meals_ratio.items(), key=lambda x:x[1], reverse=True))
    
    # Беремо найкалорійніший за співвідношенням продукт із відсортованого листа, віднімаємо його ціну від бюджету, кладемо в словник сьогоднішнього обіду
    for meal in sorted_meals_ratio.keys():
        if menu[meal]["cost"] <= budget:
            your_meal[meal] = menu[meal]["cost"]
            total_calories += menu[meal]["calories"]
            budget = budget - menu[meal]["cost"]
        
    
    return your_meal, total_calories, budget

def dynamic_programming(budget, menu):
    # Ініціалізуємо матрицю для зберігання максимальної кількості калорій
    dp = [[0] * (budget + 1) for _ in range(len(menu) + 1)]

    # Цикл для обчислення максимальної кількості калорій
    for i, (item, item_info) in enumerate(menu.items(), 1):
        for j in range(1, budget + 1):
            # Якщо ціна страви менша або рівна бюджету, ми можемо включити її
            if item_info['cost'] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_info['cost']] + item_info['calories'])
            else:
                dp[i][j] = dp[i - 1][j]

    # Відновлення оптимального набору страв
    optimal_set = []
    j = budget
    for i in range(len(menu), 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            optimal_set.append(list(menu.keys())[i - 1])
            j -= menu[list(menu.keys())[i - 1]]['cost']

    # Повертаємо результат
    return optimal_set


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


calculation = greedy_calories(100, items)
print(f"Твоє сьогоднішнє меню: {calculation[0]}")
print(f"Калорійність: {calculation[1]}")
print(f"Решта: {calculation[2]}")

calculation_2 = dynamic_programming(100, items)
print(f"Твоє сьогоднішнє меню: {calculation_2}")
