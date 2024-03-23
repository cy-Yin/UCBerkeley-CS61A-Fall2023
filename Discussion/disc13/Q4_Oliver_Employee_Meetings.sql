SELECT m.day, m.time FROM records AS r, meetings AS m 
    WHERE r.division = m.division AND r.supervisor = "Oliver Warbucks";