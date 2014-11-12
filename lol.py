import sqlite3
conn = sqlite3.connect('db.sqlite')

c = conn.cursor()
c.execute(''' CREATE TABLE adfs_match (
    "id" INTEGER PRIMARY KEY,
    "team1" varchar(30) NOT NULL,
    "team2" varchar(30) NOT NULL,
    "goal1" int NOT NULL,
    "goal2" int NOT NULL,
    "group" varchar(30) NOT NULL,
    "tour" varchar(30) NOT NULL,
    "play" varchar(30) NOT NULL,
    "date" varchar(30) NOT NULL
); ''')
conn.commit()