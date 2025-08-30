# Logrotate

## Purpose

Logrotate is a utility designed to manage log files. It automatically rotates, compresses, and mails log files. This helps to prevent log files from growing indefinitely and consuming too much disk space.

## Manual Rotation

To manually trigger log rotation for all logs defined in the configuration file, you can use the following command:

```bash
logrotate -f /opt/threat-detection-lab/logrotate/rotate-all.conf
```

## Scheduling with Cron

To automate log rotation, you can schedule it using a cron job.

1.  Open the crontab for editing:
    ```bash
    crontab -e
    ```

2.  Add the following line to run logrotate daily:
    ```cron
    0 0 * * * /usr/sbin/logrotate /opt/threat-detection-lab/logrotate/rotate-all.conf
    ```
This will execute the log rotation every day at midnight.
