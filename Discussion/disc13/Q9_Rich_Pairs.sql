SELECT a.division FROM records as a, records as b 
    WHERE a.division = b.division and a.name <> b.name 
    GROUP BY a.division HAVING COUNT(*) > 1 AND MAX(a.salary + b.salary) < 100000;


