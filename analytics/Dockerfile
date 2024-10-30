FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN apt update -y && apt install -y build-essential libpq-dev
RUN pip install --upgrade pip setuptools wheel && pip install -r requirements.txt
EXPOSE 5153
CMD ["python", "app.py"]