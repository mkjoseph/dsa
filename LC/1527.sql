-- pass 1 

SELECT * FROM patients WHERE conditions REGEXP '\\bDIAB1'

-- pass 2 

  SELECT * FROM patients WHERE conditions REGEXP '(^DIAB1|(.*\\sDIAB1))'

-- pass 3 
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%';
