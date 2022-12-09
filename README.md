# YouTube API with FastAPI

## 1. Clone Repository

```bash
git clone 
```
___


## 2. Create a virtual environment

```bash
python3 -m venv venv
```
___

## 3. Install Requirements

```bash
pip install -r requirements.txt
```
___

## 4. Run the app

```bash
uvicorn app/api:app --reload
```

# How to run the app with docker image

## 1. Build the docker image

* Go to the project directory (in where your Dockerfile is, containing your app directory).
* Build your FastAPI image:

```bash
docker build -t myimage .
```
___

## 2. Start the Docker Container

* Run a container based on your image:

```bash
docker run -d --name mycontainer -p 80:80 myimage
```
___

## 3. Interactive API docs

Now you can go to http://192.168.99.100/docs or http://127.0.0.1/docs (or equivalent, using your Docker host).

You will see the automatic interactive API documentation (provided by <a href="https://github.com/swagger-api/swagger-ui">Swagger UI</a>):

___

[![Swagger UI](./images/Screenshot%202022-12-09%20at%2023.15.50.png)](./images/Screenshot%202022-12-09%20at%2023.15.50.png)

___


