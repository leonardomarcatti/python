FROM python:3.13.9-trixie 

WORKDIR /app

COPY . .

ENV TZ="America/Sao_Paulo"

CMD ["tail", "-f", "/dev/null"]