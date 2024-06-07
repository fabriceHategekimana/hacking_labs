## Access.log file

- IP address: Pseudonymization to ensure attack patterns are still visible Potential to identify person
- Login.php GET parameters: Contain usernames and passwords
- GET session parameter: JWT with potentially personal information

## Customerdata.db file

- Customers table personal information: Names, phone number, email must be anonymized because of data protection laws.
- Customers table cc_number: Encrypted with weak encryption scheme. PCI compliance requires anonymization.
