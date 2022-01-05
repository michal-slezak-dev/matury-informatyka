SELECT "nazwa", SUM( "strzal" ) AS "suma"
FROM "klasy"
WHERE "nazwa" LIKE '%elf%'
GROUP BY "nazwa"
ORDER BY "nazwa"