# DVWA (Damn Vulnerable Web Application)

This container provides a vulnerable PHP/MySQL web application for security testing and training purposes. It is based on the official `vulnerables/web-dvwa` Docker image.

## Features

- Exposes the DVWA application on port `8080`
- Mounts Apache and MySQL logs to the host for external analysis
- Useful for testing attacks like SQL Injection and Denial of Service (DoS)

## Access

After running the container, DVWA is accessible at:

http://localhost:8080

## Mounted Logs

- logs/dvwa/apache2/access.log – incoming HTTP requests
- logs/dvwa/apache2/error.log – Apache error log
- logs/dvwa/mysql/error.log – MySQL server errors
