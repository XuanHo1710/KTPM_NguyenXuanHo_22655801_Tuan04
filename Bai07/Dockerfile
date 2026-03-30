# dùng python 3.9
FROM python:3.9-slim

WORKDIR /app

# đặt biến môi trường
ENV APP_ENV=development

# copy source code
COPY app.py .

# chạy app
CMD ["python", "app.py"]
