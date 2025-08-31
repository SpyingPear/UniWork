# Research Answers

## 1) Preserving state in HTTP apps (auth & sessions)
HTTP is stateless. Web apps preserve user state with cookies that carry a session ID. After a successful login, the server creates a session record (in memory, cache, or a database) and sends `Set-Cookie` with a secure, HTTP-only cookie. Each new request includes that cookie; the server looks up the session to identify the user and load state. Many frameworks rotate session IDs on login and use short expiries plus CSRF protection for POST requests. Some systems use signed tokens (JWTs). JWTs are self-contained and scale well, but revocation/rotation must be handled carefully. For standard Django web flows, cookie-based sessions are typical.

## 2) Django migrations to MariaDB
Install a MariaDB/MySQL driver (e.g., `mysqlclient`). In `settings.py`, set:
```python
DATABASES = {{
  "default": {{
    "ENGINE": "django.db.backends.mysql",
    "NAME": "your_db",
    "USER": "your_user",
    "PASSWORD": "your_password",
    "HOST": "your_host",
    "PORT": "3306",
    "OPTIONS": {{"charset": "utf8mb4"}},
  }}
}}
```
Ensure the MariaDB database exists and uses utf8mb4. Then run:
```bash
python manage.py makemigrations
python manage.py migrate
```
Use a least‑privilege DB user. If the DB is remote, enable TLS. Keep environments in sync by running the same migrations in each.
