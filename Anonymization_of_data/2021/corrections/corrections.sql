-- anonymize first and last name
UPDATE t_person SET first_name = substr(first_name, 1, 1) || '********';
UPDATE t_person SET last_name = substr(abs(random()), 0, 11);

-- reduce date of birth to year only
-- SELECT strftime('%Y', date_of_birth) from t_person;
UPDATE t_person SET date_of_birth = strftime('%Y', date_of_birth);

-- categorization of salaries
UPDATE t_person SET salary = "high" WHERE salary >= 100000 AND salary NOT NULL;
UPDATE t_person SET salary = "medium" WHERE salary >= 50000 AND salary < 100000 AND salary NOT NULL;
UPDATE t_person SET salary = "low" WHERE salary < 50000 AND salary NOT NULL;

-- remove data from columns is_vip, username & password
-- depending on SQLite version, dropping a column with ALTER TABLE is not supported
UPDATE t_person SET is_vip = null;
UPDATE t_person SET username = null;
UPDATE t_person SET password = null;
