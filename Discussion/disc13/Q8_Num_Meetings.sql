SELECT m.day FROM meetings as m, records as r WHERE m.division = r.division 
    GROUP BY m.day HAVING COUNT(*) < 5;


