FROM python:3.10
WORKDIR /app
COPY . /app/
RUN apt update && apt install -y ffmpeg
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "bot.py"]
