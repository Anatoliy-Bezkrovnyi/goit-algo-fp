

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
