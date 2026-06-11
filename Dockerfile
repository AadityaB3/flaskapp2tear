FROM python:3.11 AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY --from=builder /app /app

EXPOSE 5000

CMD ["python","app.py"]