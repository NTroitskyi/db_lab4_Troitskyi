import psycopg2
import matplotlib.pyplot as plt

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

    cur.execute(query1)

    total = []
    att = []
    for row in cur:
        att.append(row[0])
        total.append(row[1])

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    figure.set_size_inches(18, 10, forward=True)
    bar = bar_ax.bar(att, total, label='Total')
    bar_ax.bar_label(bar, label_type='center')
    bar_ax.set_xticks(att)

    bar_ax.set_xlabel('Користувачі')
    bar_ax.set_ylabel('Станд')
    bar_ax.set_title('Відповідність між Користувачем та Стандом із силою А')

    cur.execute(query2)

    total = []
    labels = []
    for row in cur:
        labels.append(row[0])
        total.append(row[1])

    pie_ax.pie(total, labels=labels, autopct='%1.1f%%')
    pie_ax.set_title('Користувачі з 5 сезону')

    cur.execute(query3)

    att = []
    quan = []

    for row in cur:
        att.insert(0, row[0])
        quan.insert(0, row[1])

    graph_ax.plot(att, quan, marker='o')
    graph_ax.set_xlabel('Станди')
    graph_ax.set_ylabel('Рівень')
    graph_ax.set_title('Графік залежності станду від рівня його розвитку(dev)')

plt.show()
