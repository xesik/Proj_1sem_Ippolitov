import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()

    # cur.execute("DELETE FROM bronirovanie WHERE id_tr = 1")

    # cur.execute("DELETE FROM bronirovanie WHERE id_tour = 2")

    # cur.execute("DELETE FROM bronirovanie WHERE date_br = '2022-12-15'")

    # cur.execute("DELETE FROM tourists WHERE id_tr in(SELECT id_tr FROM bronirovanie WHERE id_tour=3)")

    # cur.execute("DELETE FROM bronirovanie WHERE id_tr in(SELECT id_tr FROM tourists WHERE phone='+7(988)154-73-76')")

    # cur.execute("DELETE FROM bronirovanie WHERE id_tr in(SELECT id_tr FROM tourists WHERE email='zunagoweuzo@yandex.ru')")

    # cur.execute("DELETE FROM bronirovanie WHERE id_tour in(SELECT id_tour FROM tours WHERE date_start>'2023-10-01')")

    # cur.execute("DELETE FROM tourists WHERE id_tr in(SELECT id_tr FROM bronirovanie WHERE id_tour in(SELECT id_tour FROM tours WHERE country='Испания'))")

    # cur.execute("DELETE FROM bronirovanie WHERE id_tour in(SELECT id_tour FROM tours WHERE date_end < '2023-05-01')")

    # cur.execute("DELETE FROM bronirovanie WHERE id_tour=(SELECT id_tour FROM tours WHERE price = 4999)")

