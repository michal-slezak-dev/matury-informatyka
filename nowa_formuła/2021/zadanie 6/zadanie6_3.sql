SELECT DISTINCT "id_gracza"
FROM "jednostki"
WHERE "id_gracza" NOT IN ( SELECT "id_gracza" FROM "jednostki" WHERE "nazwa" LIKE 'artylerzysta' )
GROUP BY "id_gracza"
ORDER BY "id_gracza" ASC