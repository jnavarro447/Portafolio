FROM golang:1.12-alpine as builder

WORKDIR /usr/app/

COPY . /usr/app/

RUN apk add --no-cache libc6-compat && \
    go build main.go

FROM alpine

WORKDIR /usr/app/

COPY --from=builder /usr/app/main /usr/app

EXPOSE 4000

CMD ["./main"]