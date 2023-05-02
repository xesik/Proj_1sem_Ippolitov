# Из предложенного текстового файла (text18-28.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить текст в
# стихотворной форме предварительно вставив после строки N (N – задается пользователем)
# произвольную фразу.
# -*- coding: utf-8 -*-
text = open("text18-28.txt", "r").read()
print(f"Содержимое файла:\n{text}")
print("Количество символов в тексте:", len(text))
open("text18-28.txt", "r").close()
line_number = int(input("Введите номер строки, после которой нужно вставить фразу: "))
phrase = input("Введите фразу: ")
line = text.split("\n")   # разделение текста на строки
line.insert(line_number, phrase)   # вставка фразы в текст в списке
own_phrase = "\n".join(line)    # переделал список в текст
file = open("new_text.txt", "w")
file.write(own_phrase)
file.close()