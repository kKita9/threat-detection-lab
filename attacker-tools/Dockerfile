FROM kalilinux/kali-rolling

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Warsaw

RUN apt update && apt install -y \
    nmap \
    sqlmap \
    hydra \
    hping3 \
    curl \
    git \
    nikto \
    xsser \
    slowloris \
    metasploit-framework \
    medusa \
    python3 \
    python3-pip \
    slowhttptest \
    tzdata \
 && apt clean

 RUN git clone https://github.com/jseidl/GoldenEye /opt/goldeneye \
 && git clone https://github.com/grafov/hulk /opt/hulk

CMD [ "tail", "-f", "/dev/null" ]