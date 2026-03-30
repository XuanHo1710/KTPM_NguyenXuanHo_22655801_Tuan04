# dùng python 3.9
FROM python:3.9

# tạo thư mục app
WORKDIR /app

# copy requirements trước (optimize cache)
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy source code
COPY . .

# expose port
EXPOSE 5000

# chạy app
CMD ["python", "app.py"]
