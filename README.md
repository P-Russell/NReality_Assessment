# NReality_Assessment

## Server

The server is an AWS lambda function. The package and infrastructure is deployed by a framework called serverless.

The main file here is ./server/handler.py

This server has two endpoints:
1. Feed - accepts a post request with a users github handle and a boolean for if they want to see read later. Returns a list of feed entries.
2. Read_later - accepts a post request with a users github handle and a feed entry id. Adds that id the a list of entries that a user wants to read later and returns the id on success.

To deploy the function run `pip install -r requirements.txt && serverless deploy` inside the server directory

## Client

The client was built using a vue.js on top of a framework called Nuxt. Nuxt provides some additional help to speed up development.

The apps routes are created according to the directory structure in ./client/pages.

The code for calling the api is in ./client/plugins/api.js

There is an implementation of vuex in ./client/store/index.js

The components are found in the ./client/components` directory.

To run this app locally `npm run dev` inside the client directory


## Problems With app
* The read later list is not tied to a specific session. If a user sets that entry to read later that entry will be read later for all users