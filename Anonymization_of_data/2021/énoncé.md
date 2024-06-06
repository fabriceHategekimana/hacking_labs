# Introduction

Before a database is passed to a third party for statistical analysis of salaries, the data must be anonymized.
Goal and Tasks

Anonymize the data according to the following requirements:

- First names: Keep the first character of the first name and replace any further characters by exactly 9 asterisks (*). Example: "Mike" is changed to "M*********"

- Last names: Replace all last names with a random number of 10 digits.

- Date of birth: Reduce the date to the year. Example: 01.01.1999 is changed to 1999 only.

- Salary: Reduce the precision of data by replacing the salary with the correct category according the following rules:
	
	- low:	salaries less than 50k
	- medium:	salaries from exactly 50k to less than 100k
	- high:	salaries from exactly 100k and upwards

- Remove all usernames, password hashes and the VIP status.

# Submission

Submit a ZIP archive containing the database file with the anonymized data and a written report as PDF document with a brief technical description of your approach (including information about any methods, tools, commands, scripts etc. used).
