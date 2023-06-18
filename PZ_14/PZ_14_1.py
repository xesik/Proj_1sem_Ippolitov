# -*- coding: utf-8 -*-
import re

with open("dates.txt", "r") as f:  # открываем файл для чтения
    text = f.read()
dates_dot = re.findall(r"\b\d{2}\.\d{2}\.\d{4}\b", text)  # находим все даты
dates_slash = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)
count_dot = len(dates_dot)
count_slash = len(dates_slash)
with open("february_dates.txt", "w") as f:  # открываем файл для записи значения
    february_dates_dot = re.findall(r"\b\d{2}\.02\.\d{4}\b", text)
    for date in february_dates_dot:
        date_slash = re.sub(r"\.", "/", date)
        f.write(date_slash + "\n")

print("Количество дат в формате ДД.ММ.ГГГГ:", count_dot)
print("Количество дат в формате ДД/ММ/ГГГГ:", count_slash)
