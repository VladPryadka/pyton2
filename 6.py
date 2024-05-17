counter = 0

# Первый вопрос
answer = input("Столица России?")
if answer == "Москва" or answer == "москва":
    counter = counter + 1
    print("Вы ответили верно")
else:
    print("Вы ответили неверно")

# Второй вопрос
answer = input("Какой язык мы изучаем?")
if answer == "Python" or answer == "Пайтон":
    counter = counter + 1
    print("Вы ответили верно")
else:
    print("Вы ответили неверно")

# Третий вопрос
answer = input("Сколько континентов на планете Земля?")
if answer == "6" or answer == "шесть":
    counter = counter + 1
    print("Вы ответили верно")
else:
    print("Вы ответили неверно")

# Четвертый вопрос
answer = input("Кто написал 'Война и мир'?")
if answer == "Толстой" or answer == "толстой":
    counter = counter + 1
    print("Вы ответили верно")
else:
    print("Вы ответили неверно")

# Вывод результата
print(f"Вы набрали баллов: {counter}")