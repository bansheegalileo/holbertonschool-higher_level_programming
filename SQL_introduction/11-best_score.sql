-- Lists scores greater than/equal to 10 in second_table.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
