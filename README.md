# NReality_Assessment

## Server

The server is an AWS lambda function. The package and infrastructure is deployed by a framework called serverless.

The main file here is ./server/handler.py

To deploy the function run `pip install -r requirements.txt && serverless deploy` inside the server directory

## Client

The client was built using a vue.js on top of a framework called Nuxt. Nuxt provides some additional help to speed up development.

The apps routes are created according to the directory structure in ./client/pages.

The code for calling the api is in ./client/plugins/api.js

There is an implementation of vuex in ./client/store/index.js

The components are found in the ./client/components` directory.

To run this app locally `npm run dev` inside the client directory