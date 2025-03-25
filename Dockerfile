FROM python:3.13
WORKDIR /app
COPY src/config.py .
COPY src/bot.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "bot.py"]