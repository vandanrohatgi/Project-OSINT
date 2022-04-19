FROM node:alpine
WORKDIR /frontend
EXPOSE 3000
COPY . .
RUN npm i
RUN npm run build
CMD ["npm","run","start"]