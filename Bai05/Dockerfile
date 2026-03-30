# Stage 1: build Go binary
FROM golang:1.21-alpine AS build

WORKDIR /app

COPY go.mod .
COPY main.go .

RUN go build -o app main.go

# Stage 2: chạy binary
FROM alpine:latest

WORKDIR /app

COPY --from=build /app/app .

EXPOSE 8080

CMD ["./app"]
