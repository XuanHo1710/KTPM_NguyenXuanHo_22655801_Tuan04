# dùng nginx latest
FROM nginx:latest

# copy file html vào thư mục mặc định của nginx
COPY index.html /usr/share/nginx/html/index.html

# expose port
EXPOSE 80

# chạy nginx
CMD ["nginx", "-g", "daemon off;"]
