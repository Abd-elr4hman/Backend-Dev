# Task-Manager-API
A simple RESTfull CRUD API Implemented with Node.js+Express and Python+FastAPI.

# How to run
### Node version:
```
cd Node+Express
nodemon start
```

### FastAPI version:
```
cd Python+FastAPI
uvicorn app:app --port 3000 --reload
```

# Test with Postman collection
[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/20861561-87190136-6920-4809-a81d-77bd49018793?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D20861561-87190136-6920-4809-a81d-77bd49018793%26entityType%3Dcollection%26workspaceId%3Debcdedd2-fbc8-46bc-95f1-bfb7d7b18460)

## Goals:
* [x] Build highly scalable RESTful API's to create, read, update and delete data from a mongodb database.
* [x] Implement validation for endpoints to ensure that the data being entered is valid.
* [x] Implement pagination, sorting and filtering for get endpoints.
* [x] Use docker to build API containers.
* [x] Use kubernetes to deploy and manage containerized APIs.
* [ ] Use nginx as ingress controller to expose APIs to the internet.
* [ ] Implement horizontal pod autoscalling.
* [ ] Use prometheus and grafana to monitor the performance and health of APIs.
* [ ] Use kubernetes secrets to securely store the sensitive information.
