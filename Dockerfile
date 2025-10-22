FROM python:3.13.9-trixie 

WORKDIR /app

COPY . .

CMD ["tail", "-f", "/dev/null"]