--Вивести ім'я користувача та назву станду з показником сили А
SELECT user_name, stand_name, stand.pwr as stand_power FROM stand_user, stand
WHERE stand_user.id_stand = stand.id_stand 
AND stand.pwr like 'A'

--Вивести імена користувачів, які зустрічаються в 5 сезоні
SELECT user_name, season_num as stand_power FROM stand_user, season
WHERE stand_user.id_season = season.id_season
AND season.season_num = 5

--Вивести всі станди за зменшенням рівня розвитку здібностей(dev)
SELECT stand_name, dev FROM stand
ORDER BY CASE
		 WHEN dev = 'I' then 1
		 WHEN dev = 'A' then 2
		 WHEN dev = 'B' then 3
		 WHEN dev = 'C' then 4
		 WHEN dev = 'D' then 5
		 WHEN dev = 'E' then 6
		 END ASC