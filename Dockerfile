FROM node:18.15.0-alpine3.17

WORKDIR /usr/src/app

COPY . .
RUN apk update && apk add git
RUN apk add --no-cache python3-dev libxml2-dev libxslt-dev gcc musl-dev
RUN apk add --no-cache py3-pip
RUN apk add py3-requests
RUN pip3 install beautifulsoup4
RUN apk add openssl libsasl libcrypto1.1
RUN pip3 install pymongo
#RUN git clone https://github.com/ketanlotake/myapp.git /usr/src/app
RUN npm install --production
