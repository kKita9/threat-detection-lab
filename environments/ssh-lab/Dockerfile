FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Use a reliable mirror and install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends openssh-server rsyslog && \
    mkdir -p /var/run/sshd /var/log && \
    touch /var/log/auth.log && \
    rm -rf /var/lib/apt/lists/*

# Set root password
RUN echo 'root:root123' | chpasswd

# Configure SSH to allow root login, password auth, and verbose logging
RUN sed -i 's/#*PermitRootLogin .*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#*PasswordAuthentication .*/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/#*LogLevel .*/LogLevel VERBOSE/' /etc/ssh/sshd_config

# Make sure rsyslog loads the kernel log module (optional)
RUN sed -i 's/^#module(load="imklog")/module(load="imklog")/' /etc/rsyslog.conf || true

# Add and set permissions on startup script
COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 22

CMD ["/start.sh"]

