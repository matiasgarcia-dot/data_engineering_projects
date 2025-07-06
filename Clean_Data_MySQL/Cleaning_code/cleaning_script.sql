-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS clean;
USE clean;

-- Rename malformed columns from the CSV import
ALTER TABLE data
CHANGE COLUMN `ï»¿Id?empleado` Id_emp VARCHAR(20) NULL,
CHANGE COLUMN `gÃ©nero` Gender VARCHAR(20) NULL;

-- Check for duplicate employee IDs
SELECT Id_emp, COUNT(*) AS duplicate_count
FROM data
GROUP BY Id_emp
HAVING COUNT(*) > 1;

-- Count total number of duplicate records
SELECT COUNT(*) AS total_duplicates
FROM (
    SELECT Id_emp
    FROM data
    GROUP BY Id_emp
    HAVING COUNT(*) > 1
) AS sub;

-- Remove duplicates using a temporary table
RENAME TABLE data TO dataRaw;

CREATE TEMPORARY TABLE temp_data AS
SELECT DISTINCT * FROM dataRaw;

CREATE TABLE clean AS
SELECT * FROM temp_data;

-- Drop the original table
DROP TABLE dataRaw;

-- Rename columns to standard English-friendly names
ALTER TABLE clean
CHANGE COLUMN Apellido LastName VARCHAR(50) NULL,
CHANGE COLUMN star_date start_date VARCHAR(50) NULL;

-- Trim leading/trailing spaces from 'name' and 'LastName' fields
UPDATE clean SET name = TRIM(name)
WHERE LENGTH(name) != LENGTH(TRIM(name));

UPDATE clean SET LastName = TRIM(LastName)
WHERE LENGTH(LastName) != LENGTH(TRIM(LastName));

-- Normalize multiple spaces into a single space in 'area' column
UPDATE clean
SET area = TRIM(REGEXP_REPLACE(area, '\s+', ' '))
WHERE area REGEXP '\s{2,}';

-- Standardize gender values: convert to English and lowercase
UPDATE clean
SET Gender = CASE
    WHEN TRIM(LOWER(Gender)) = 'hombre' THEN 'male'
    WHEN TRIM(LOWER(Gender)) = 'mujer' THEN 'female'
    ELSE Gender
END;

-- Clean salary column: remove dollar sign and commas
UPDATE clean
SET salary = TRIM(REPLACE(REPLACE(salary, '$', ''), ',', ''));

-- Convert salary column from text to DECIMAL format
ALTER TABLE clean MODIFY COLUMN salary DECIMAL(10,2);

-- Convert start_date from text to DATE format
ALTER TABLE clean ADD COLUMN start_date_clean DATE;

UPDATE clean
SET start_date_clean = STR_TO_DATE(start_date, '%m/%d/%Y');

-- Replace the original start_date column with the cleaned one
ALTER TABLE clean DROP COLUMN start_date;
ALTER TABLE clean CHANGE COLUMN start_date_clean start_date DATE;

-- Remove the 'type' column since it is no longer needed
ALTER TABLE clean DROP COLUMN type;

-- Delete records where 'name' is missing or blank
DELETE FROM clean
WHERE name IS NULL OR name = '';

-- Create index on 'Id_emp' column to improve performance
CREATE INDEX idx_id_emp ON clean(Id_emp);

-- Remove unnecessary columns (if present)
ALTER TABLE clean DROP COLUMN finish_date;
ALTER TABLE clean DROP COLUMN promotion_date;

-- Create a stored procedure to easily query the clean data
DELIMITER //
CREATE PROCEDURE limp()
BEGIN
    SELECT * FROM clean;
END;
//
DELIMITER ;

-- Call the procedure to view cleaned data
CALL limp();

-- Final preview and validation
SELECT * FROM clean;

-- Check unique values for type (will show nothing since it's dropped)
SELECT DISTINCT type FROM clean;

-- Check all unique salary values (sorted)
SELECT DISTINCT salary FROM clean ORDER BY salary DESC;

-- Format and check all start dates
SELECT DISTINCT DATE_FORMAT(start_date, '%Y-%m-%d') AS formatted_startdate FROM clean;
