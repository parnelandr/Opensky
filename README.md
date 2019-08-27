# Opensky
This repo is built on the api for opensky-network (more information here: https://opensky-network.org/apidoc/)

Currently it includes:

- configuration for building a database for flight positions.
- a sample database.
- an API built on top of flask and connexion libraries. GET and POST operations.
- swagger documentation for the API.
- a simple scheduler script to request positions from the opensky-network and POST into database.
- a template for a front-end application built over top.

Future plans:

- include installation documentation
- build application out showing most recent positions in database
