SELECT a.name FROM records as a, records as b 
    WHERE a.supervisor = b.name AND a.division <> b.division;


