FROM node:18.15.0-alpine3.17

WORKDIR /usr/src/app

#COPY . .
RUN apk update && apk add git
RUN git clone https://github.com/ketanlotake/test.git .
RUN echo ls -lrt
RUN npm install --production