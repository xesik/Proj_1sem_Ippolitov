# Книжные магазины предлагают следующие коллекции книг.
# Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет – Пушкин, Достоевский, Маяковский.
# Галерея – Чехов, Тютчев, Пушкин.
# Определить в каких магазинах
# можно приобрести книги Пушкина и Тютчева
magistr = {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"}
dombooks = {"Толстой", "Грибоедов", "Чехов", "Пушкин"}
bookmarket = {"Пушкин", "Достоевский", "Маяковский"}
galereya = {"Чехов", "Тютчев", "Пушкин"}
if "Пушкин" in magistr and "Тютчев" in magistr:    # Проверка на наличие Пушкина и Тютчева
    print("magistr")
if "Пушкин" in dombooks and "Тютчев" in dombooks:
    print("domKnigi")
if "Пушкин" in bookmarket and "Тютчев" in bookmarket:
    print("bukMarket")
if "Пушкин" in galereya and "Тютчев" in galereya:
    print("galereya")