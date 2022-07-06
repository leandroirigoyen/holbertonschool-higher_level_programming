-- Script that lists all reords of the table second_table
SELECT score,name FROM second_table WHERE name RLIKE '^[A-Z]' ORDER BY score DESC;
