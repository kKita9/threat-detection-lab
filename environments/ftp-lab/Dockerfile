FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y vsftpd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Test user
RUN useradd -m testuser && \
    echo "testuser:test123" | chpasswd

# Copy configuration and start file
COPY vsftpd.conf /etc/vsftpd.conf
COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 21

CMD ["/start.sh"]

