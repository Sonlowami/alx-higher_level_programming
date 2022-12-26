-- List number of records with same score
SELECT score, COUNT(score) FROM second_table GROUP BY score;
