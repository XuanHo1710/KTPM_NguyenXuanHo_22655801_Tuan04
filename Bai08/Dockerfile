# dùng postgres 15
FROM postgres:15

# copy file SQL vào thư mục init của postgres
# postgres tự động chạy các file trong /docker-entrypoint-initdb.d/ khi khởi tạo lần đầu
COPY init.sql /docker-entrypoint-initdb.d/

# expose port
EXPOSE 5432
