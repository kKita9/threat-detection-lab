FTP Lab

This container provides FTP server based on vsftpd, intended for brute-force and logging experiments in a threat detection lab environment.

Setup

The image is based on ubuntu:22.04. It installs vsftpd, adds a test user, and applies a custom configuration.

Credentials
- Username: testuser
- Password: test123

Ports
- Exposes port 21 internally
- Port 2121 is used on the host (defined in docker-compose.yml)

Configuration

The file vsftpd.conf defines:
- Disabled anonymous access
- Enabled local users and write permissions
- Log file set to /var/log/vsftpd.log
- Logging of FTP protocol and transfers

▶️ Usage

Start with Docker Compose:

docker compose up -d --build

Test

Use any FTP client or command-line:

ftp 127.0.0.1 2121

Then log in using the credentials above. After login attempts or file activity, logs will appear in:

logs/ftp-lab/vsftpd.log

Volumes

The log file is mounted to the host via:

- ./logs/ftp-lab/vsftpd.log:/var/log/vsftpd.log

Make sure the file exists before starting the container (created in init.sh).
