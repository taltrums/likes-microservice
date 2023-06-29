# Likes Microservice

## Running the Application

1. Install [docker](https://docs.docker.com/engine/install/ubuntu/) and [docker-compose](https://docs.docker.com/compose/install/linux/#install-the-plugin-manually)

2. Run the data base using 

```
sudo docker compose -d flask_db
```
3. Run the whole application

```code
sudo docker compose up -d flask_app
```
This will spin up the application and necessary files to run.

## Application Architecture - 

Preview [Application Architecture](https://drive.google.com/file/d/1CFswREFHfenRdeTtm7Ym8zynVCNQShaX/view)

## Testing the Application with postman - 
After the application containers starts running you can make the following requests - 

1. POST API Call for Like Events - 
http://127.0.0.1:5000/likes 
This endpoint will register a like for a particular content.

2. GET API Call for Like Check - 
http://127.0.0.1:5000/likes/check
This endpoint will check for whether a particular content is liked or not.

3. GET API CALL for like Count - 
http://127.0.0.1:5000/likes/total
This endpoint will return the total no of likes for a particular content

## Documentation

Preview [API Documentation](https://documenter.getpostman.com/view/13971988/2s93z9ciL8)