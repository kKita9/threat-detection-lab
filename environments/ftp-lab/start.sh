#!/bin/bash
service vsftpd restart
tail -f /var/log/vsftpd.log

