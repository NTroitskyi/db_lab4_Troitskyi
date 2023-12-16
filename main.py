import psycopg2


username = 'postgres'
password = ''
database = 'jojo'
host = 'localhost'
port = '5433'

query1 = '''SELECT user_name, stand_name, stand.pwr as stand_power FROM stand_user, stand
WHERE stand_user.id_stand = stand.id_stand 
AND stand.pwr like 'A'
'''


query2 = '''SELECT user_name, season_num as stand_power FROM stand_user, season
WHERE stand_user.id_season = season.id_season
AND season.season_num = 5
'''


query3 = '''SELECT stand_name, dev FROM stand
ORDER BY CASE
		 WHEN dev = 'I' then 1
		 WHEN dev = 'A' then 2
		 WHEN dev = 'B' then 3
		 WHEN dev = 'C' then 4
		 WHEN dev = 'D' then 5
		 WHEN dev = 'E' then 6
		 END ASC
		 '''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
    print("Database opened successfully")
    cur = conn.cursor()

    print("Вивести ім'я користувача та назву станду з показником сили А: ")
    cur.execute(query1)

    for row in cur:
        print(row)

    print("Вивести імена користувачів, які зустрічаються в 5 сезоні: ")
    cur.execute(query2)

    for row in cur:
        print(row)

    print("Вивести всі станди за зменшенням рівня розвитку здібностей(dev): ")
    cur.execute(query3)

    for row in cur:
        print(row)