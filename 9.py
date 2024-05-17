import turtle

# Настройка черепашки
turtle.speed(1)  # Устанавливаем скорость

# Рисуем нижний круг снеговика
turtle.penup()  # Поднять перо
turtle.goto(0, -200)  # Перемещаемся в начальную точку
turtle.pendown()  # Опустить перо
turtle.color("blue")  # Устанавливаем цвет
turtle.begin_fill()
turtle.circle(100)  # Рисуем круг радиусом 100
turtle.end_fill()

# Рисуем средний круг снеговика
turtle.penup()  # Поднять перо
turtle.goto(0, -50)  # Перемещаемся в новую точку
turtle.pendown()  # Опустить перо
turtle.color("lightblue")  # Устанавливаем цвет
turtle.begin_fill()
turtle.circle(80)  # Рисуем круг радиусом 80
turtle.end_fill()

# Рисуем верхний круг снеговика (голову)
turtle.penup()  # Поднять перо
turtle.goto(0, 50)  # Перемещаемся в новую точку
turtle.pendown()  # Опустить перо
turtle.color("white")  # Устанавливаем цвет
turtle.begin_fill()
turtle.circle(60)  # Рисуем круг радиусом 60
turtle.end_fill()

# Завершение рисования
turtle.done()



import turtle

# Функция для рисования многоугольника
def draw_polygon(sides, color):
    angle = 360 / sides
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(sides):
        turtle.forward(100)
        turtle.right(angle)
    turtle.end_fill()

# Запрос у пользователя данных
num_sides = int(input("Введите количество углов многоугольника: "))
color = input("Введите цвет многоугольника: ")

# Рисование многоугольника
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
draw_polygon(num_sides, color)

# Завершение рисования
turtle.done()