# Задаем курсы валют (условные)
usd_rate = 0.013
eur_rate = 0.012
cny_rate = 0.08

# Запрос суммы в рублях от пользователя
rub_amount = float(input("Введите сумму в рублях: "))

# Запрос выбора валюты для конвертации
currency = input("Введите валюту для конвертации (USD, EUR, CNY): ").upper()

# Конвертация валюты
if currency == "USD":
    converted_amount = rub_amount * usd_rate
    print(f"{rub_amount} рублей = {converted_amount} долларов США")
elif currency == "EUR":
    converted_amount = rub_amount * eur_rate
    print(f"{rub_amount} рублей = {converted_amount} евро")
elif currency == "CNY":
    converted_amount = rub_amount * cny_rate
    print(f"{rub_amount} рублей = {converted_amount} китайских юаней")
else:
    print("Неизвестная валюта")