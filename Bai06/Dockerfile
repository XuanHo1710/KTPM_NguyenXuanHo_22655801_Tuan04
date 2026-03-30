# Stage 1: build code bằng node:18
FROM node:18 AS build

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

RUN npm run build

# Stage 2: chạy ứng dụng bằng node:18-alpine (nhẹ hơn)
FROM node:18-alpine

WORKDIR /app

COPY --from=build /app .

EXPOSE 3000

CMD ["npm", "start"]
