import turtle

def pifagor_tree(x, y, size, angle, depth):
    if depth == 0:
        return
    else:
        turtle.penup()
        turtle.goto(x, y)
        turtle.setheading(angle)
        turtle.pendown()
        turtle.forward(size)
        new_x = turtle.xcor()
        new_y = turtle.ycor()
        pifagor_tree(new_x, new_y, size * 0.7, angle + 45, depth - 1)
        pifagor_tree(new_x, new_y, size * 0.7, angle - 45, depth - 1)

x = 0 # Початкові координати дерева "x"
y = 0 # Початкові координати дерева "у"
size = 150 # Розмір дерева
angle = 50 # Кут між гілками дерева
depth = 9 # Глибина рекурсії дерева


turtle.setup(width=800, height=800)  # Задаємо розмір вікна
turtle.speed(0)  # Задаємо максимальну швидкість виконання
turtle.color("red")  # Задаємо колір для ліній
turtle.penup()
turtle.goto(0, -300)  # Переміщаємо відрізок на початок координат
turtle.pendown()
pifagor_tree(x, y, size, angle, depth)  # Визначаємо параметри дерева (початкові координати, розмір, кут, глибина)
turtle.done()