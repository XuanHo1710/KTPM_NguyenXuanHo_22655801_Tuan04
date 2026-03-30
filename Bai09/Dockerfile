# dùng redis latest
FROM redis:latest

# copy file config vào container
COPY redis.conf /usr/local/etc/redis/redis.conf

# expose port
EXPOSE 6379

# chạy redis với config tùy chỉnh
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]
