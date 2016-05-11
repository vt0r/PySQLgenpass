PySQLgenpass
========

This script takes password input on stdin and does a double-SHA1 hash on it to produce MySQL password hashes.
  
Since the password is not echoed to STDOUT, it's a bit safer for shell/MySQL client history than the usual methods, such as:
```sql
SELECT PASSWORD('blah');
```
The password is read twice to ensure both entries match.
