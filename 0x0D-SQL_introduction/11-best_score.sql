-- show only scores > 10 descending
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;