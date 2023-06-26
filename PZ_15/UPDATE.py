import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()

# cur.execute("UPDATE tours SET date_start = '2023-05-01' WHERE id_tour = 1")

# cur.execute("UPDATE tours SET price = 1500 WHERE id_tour = 7")

# cur.execute("UPDATE tourists SET phone = '+1(555)123-4567' WHERE id_tr = 5")

# cur.execute("UPDATE bronirovanie SET date_br = '2023-04-05' WHERE id_br = 3")

# cur.execute("UPDATE bronirovanie SET kol = 3 WHERE id_br = 8")

# cur.execute("UPDATE tours SET date_end = '2023-08-21' WHERE id_tour = 2")

# cur.execute("UPDATE tourists SET email = 'new_email@example.com' WHERE id_tr = 1")

# cur.execute("UPDATE tours SET date_start = '2023-06-15' WHERE id_tour = 4")

# cur.execute("UPDATE tours SET date_start = '2023-05-01' WHERE country = 'Испания'")

# cur.execute("UPDATE tours SET price = 1500 WHERE name_tour = 'Греция - отдых на море'")

# cur.execute("UPDATE tours SET date_start = '2023-06-01' WHERE name_tour = 'Испания - путешествие по городам'")

# cur.execute("UPDATE bronirovanie SET kol = 3 WHERE id_br = 1002")

# cur.execute("UPDATE tourists SET phone = '+1(123)456-7890' WHERE id_tr = 2001")

# cur.execute("UPDATE tours SET date_start = '2024-07-01' WHERE price < 2000")

# cur.execute("UPDATE tourists SET email = 'new_email@example.com' WHERE phone LIKE '+7%'")

# НУЖЕН ИННЕР ДЖОИН # cur.execute("UPDATE tours SET date_start = '2023-08-15' WHERE (SELECT kol FROM bronirovanie)>2")

# НУЖЕН ИННЕР ДЖОИН # cur.execute("UPDATE tours SET name_tour = '2023-08-15' WHERE (SELECT kol FROM bronirovanie)>2")
