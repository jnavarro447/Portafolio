FROM node

WORKDIR /usr/app/

COPY . /usr/app/

RUN npm init --yes

RUN npm install

EXPOSE 3000

CMD ["node", "helloWorld.js"]
