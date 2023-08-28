FROM python:latest

RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . /usr/src/bot

CMD ["python3", "bot.py"]