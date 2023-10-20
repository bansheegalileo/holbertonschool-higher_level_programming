-- Prints the description of the table first_table from the database hbtn_0c_0.
SELECT CONCAT('Table   Create Table\n', TABLE_NAME, '     ', CREATE_TABLE)
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
