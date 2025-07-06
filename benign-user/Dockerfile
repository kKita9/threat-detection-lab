FROM python:3.11-slim

WORKDIR /app

COPY benign-user/activity_generator.py ./
COPY benign-user/activities/ ./activities/
# COPY benign-user/user_activity.yaml ./
COPY common/ ./common/

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        inetutils-ftp \
        curl \
        sshpass \
        openssh-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pyyaml

CMD ["python", "activity_generator.py"]
