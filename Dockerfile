FROM python:3.13.9-trixie 

WORKDIR /app

RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --no-cache-dir mysql-connector-python

COPY . .

ENV TZ="America/Sao_Paulo"

CMD ["tail", "-f", "/dev/null"]