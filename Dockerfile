FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
RUN pip install --upgrade pip
COPY . /usr/src/app
RUN pip install -r ./requirements.txt
ENTRYPOINT python weather_bot.py