import os
import sqlite3 as sq

path = '..\PZ_15\saper.db'
os.remove(path)
tourists = [
    (2001, "Максим", "Домрин", "м", "1989-08-05", "+7(988)300-96-78", "robben10344@gmail.com"),
    (1002, "Никита", "Вяткин", "ж", "2005-07-20", "+7(988)819-35-99", "suhariki52@mail.ru"),
    (1003, "Родион", "Ипполитов", "м", "1980-02-14", "+8(988)430-45-85", "sonnayabebra@yandex.ru"),
    (1, "Николай", "Меняйло", "м", "2001-09-23", "+7(988)663-71-81", "veiquafrabreubu@mail.ru"),
    (2, "Ярослав", "Туманов", "м", "1999-12-2", "+7(988)154-73-76", "kommaubrigregroi@gmail.com"),
    (3, "Ангелина", "Павленко", "ж", "2004-6-14", "+9(988)258-43-82", "pregrefoifroiquo@yandex.ru"),
    (4, "Ирина", "Баломутова", "ж", "1977-8-11", "+7(988)333-22-07", "zunagoweuzo@yandex.ru"),
    (5, "Артут", "Саркисян", "м", "2000-5-23", "+6(988)352-92-42", "meillesawessa@gmail.com"),
    (6, "Максим", "Полянский", "м", "1982-6-19", "+6(988)961-34-86", "fucubreizaha@mail.ru"),
    (7, "Андрей", "Тарабукин", "м", "2007-5-25", "+7(988)412-41-40", "vobixeheroi@mail.ru"),
]
tour = [
    (1, "Греция - отдых на море", "Греция", "Афины", "2023-04-01", "2023-04-10", "4999"),
    (2, "Тур в Китай", "Китай", "Гонконг", "2023-05-12", "2023-05-22", "24440"),
    (1003, "Тур в Мадагаскар", "Мадагаскар", "Масуала", "2023-06-12", "2023-06-17", "2000"),
    (4, "Тур в Словакию", "Словакия", "Братислава", "2023-07-15", "2023-07-27", "16300"),
    (5, "Испания - путешествие по городам", "Испания", "Барселона", "2023-10-12", "2023-10-21", "15200"),
    (6, "Тур в ОАЭ", "ОАЭ", "Дубай", "2023-06-24", "2023-07-01", "50200"),
    (7, "Тур в Казахстан", "Казахстан", "Алматы", "2023-04-05", "2023-04-09", "3500"),
    (8, "Египет - отдых на курорте", "Египет", "Каир", "2023-05-12", "2023-05-17", "9500"),
    (9, "Тур в США", "США", "Нью-Йопрк", "2023-08-04", "2023-08-04", "24600"),
    (3, "Тур в Филлипины", "Филлинпины", "Остров Боракай", "2023-06-12", "2023-06-15", "95000"),
]
bronirovanie = [
    (1001, 1, 4, "2023-01-10", "210"),
    (1002, 2, 8, "2023-02-22", "134"),
    (1003, 3, 1003, "2023-01-14", "2"),
    (3, 4, 1, "2023-01-29", "205"),
    (5, 5, 5, "2022-12-22", "401"),
    (6, 7, 8, "2022-12-15", "222"),
    (7, 6, 7, "2022-11-24", "472"),
    (8, 1002, 2, "2022-11-24", "669"),
    (9, 1003, 6, "2022-12-01", "347"),
    (10, 2001, 3, "2023-02-14", "746"),
]
with sq.connect('saper.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS tourists (
 id_tr INTEGER PRIMARY KEY,
 name VARCHAR,
 surname VARCHAR,
 sex VARCHAR,
 birthday DATE,
 phone VARCHAR,
 email VARCHAR
 )""")
cur.execute("""CREATE TABLE IF NOT EXISTS tours (
 id_tour INTEGER PRIMARY KEY,
 name_tour VARCHAR,
 country VARCHAR,
 city VARCHAR,
 date_start DATE,
 date_end DATE,
 price DECIMAL
 )""")
cur.execute("""CREATE TABLE IF NOT EXISTS bronirovanie (
 id_br INTEGER PRIMARY KEY,
 id_tr VARCHAR,
 id_tour VARCHAR,
 date_br DATE,
 kol INTEGER,
 FOREIGN KEY (id_tr) REFERENCES tourists(id_tr),
 FOREIGN KEY (id_tour) REFERENCES tours(id_tour)
 )""")
with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO tourists VALUES (?, ?, ?, ?, ?, ?, ?)", tourists)
    cur.executemany("INSERT INTO tours VALUES (?, ?, ?, ?, ?, ?, ?)", tour)
    cur.executemany("INSERT INTO bronirovanie VALUES (?, ?, ?, ?, ?)", bronirovanie)
    cur.execute("SELECT name, surname FROM tourists")
    result = cur.fetchall()
    print(f"1\n{result}")
    cur.execute("SELECT name_tour FROM tours ORDER BY price DESC")
    result = cur.fetchall()
    print(f"2\n{result}")
    cur.execute(
        "SELECT id_br FROM bronirovanie INNER JOIN tours ON tours.id_tour = bronirovanie.id_tour WHERE "
        "city='Братислава'")
    result = cur.fetchall()
    print(f"3\n{result}")
    cur.execute("SELECT name, surname ,date_br FROM tourists INNER JOIN bronirovanie ON tourists.id_tr = bronirovanie.id_tr WHERE date_br = '2022-11-24'")
    result = cur.fetchall()
    print(f"4\n{result}")
    cur.execute("SELECT name_tour, country, city FROM tours")
    result = cur.fetchall()
    print(f"5\n{result}")
    cur.execute("SELECT name, surname FROM tourists WHERE sex = 'ж' AND birthday > '1990-01-01'")
    result = cur.fetchall()
    print(f"6    Никита на самом деле женщина(так и задумано)\n{result}")
    cur.execute("SELECT name_tour FROM tours WHERE price > 5000")
    result = cur.fetchall()
    print(f"7\n{result}")
    cur.execute("SELECT name, surname FROM tourists INNER JOIN bronirovanie ON tourists.id_tr = bronirovanie.id_tr WHERE id_tour = 8")
    result = cur.fetchall()
    print(f"8\n{result}")
    cur.execute("SELECT name, surname FROM tourists INNER JOIN bronirovanie ON tourists.id_tr = bronirovanie.id_tr WHERE id_tour = 8 AND date_br = '2022-12-15'")
    result = cur.fetchall()
    print(f"9\n{result}")
    cur.execute("SELECT name, surname FROM tourists WHERE phone LIKE '+7%'")
    result = cur.fetchall()
    print(f"10\n{result}")
