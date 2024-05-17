import turtle

# Настройка черепашки
turtle.speed(1)  # Устанавливаем скорость

# Рисуем основание дома
turtle.penup()  # Поднять перо
turtle.goto(-100, -100)  # Начальная позиция
turtle.pendown()  # Опустить перо
turtle.forward(200)  # Нарисовать сторону длиной 200 пикселей
turtle.left(90)  # Повернуть на 90 градусов
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)

# Рисуем крышу
turtle.left(45)  # Поворот для рисования крыши
turtle.forward(140)  # Длина крыши
turtle.right(90)  # Поворот для рисования второй стороны крыши
turtle.forward(140)
turtle.right(45)  # Возврат в исходное положение

# Завершаем рисование
turtle.hideturtle()  # Скрыть черепашку
turtle.done()