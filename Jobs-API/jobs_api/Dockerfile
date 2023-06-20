FROM node:9-slim
WORKDIR /app
EXPOSE 3000
COPY package-lock.json /app
RUN npm install
COPY . /app
CMD ["npm", "start"]