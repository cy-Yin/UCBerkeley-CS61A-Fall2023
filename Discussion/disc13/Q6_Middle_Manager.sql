SELECT a.name FROM records as a, records as b 
    WHERE a.name = b.supervisor AND b.supervisor <> b. name;


