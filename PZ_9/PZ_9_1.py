# Организовать словарь 10 русско- английских слов, обеспечивающий
# "перевод" русского слова на английского.
slovar = {"привет": "hello",
          "пока": "bye",
          "муравей": "ant",
          "вода": "water",
          "земля": "earth",
          "животное": "animal",
          "дерево": "tree",
          "деление": "division",
          "умножение": "multiplication",
          "оружие": "gun"}
slovo = input("Введите слово: ")
if slovo in slovar:
    print(f"Результат перевода: {slovar[slovo]}")
else:
    quit()
