SELECT "kraj", COUNT( DISTINCT "id_gracza" ) AS "liczba_graczy"
FROM "gracze"
WHERE YEAR( "data_dolaczenia" ) LIKE '2018'
GROUP BY "kraj"
ORDER BY "liczba_graczy" DESC LIMIT 5