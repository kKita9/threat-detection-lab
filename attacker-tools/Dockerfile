FROM kalilinux/kali-rolling

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Warsaw

RUN apt update && apt install -y \
    nmap \
    sqlmap \
    hydra \
    hping3 \
    curl \
    tzdata

CMD [ "tail", "-f", "/dev/null" ]