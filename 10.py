import turtle

turtle.shape("turtle")
turtle.speed(5)

angle = int(input("Введите количество углов: "))
size = int(input("Введите длину стороны: "))
color = input("Введите цвет: ")

# Максимальное количество углов, которое может нарисовать черепашка
# Можно установить любое значение в зависимости от ваших требований
max_angle = 5

turtle.color(color)

if angle < 3:
    print("Углов не может быть меньше трёх")
elif angle > max_angle:
    print(f"Черепашка не может нарисовать фигуру с {angle} углами")
else:
    for i in range(angle):
        turtle.forward(size)
        turtle.left(360 / angle)

turtle.done()