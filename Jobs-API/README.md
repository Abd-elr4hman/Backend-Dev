# Jobs-API
A simple RESTfull CRUD API Implemented with Node.js+Express and Python+FastAPI.

# How to run
### Node version:
```
cd jobs_api
nodemon start
```

# Test with Postman collection
[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/20861561-6eea2f90-691a-4c16-918f-a5b44dd38837?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D20861561-6eea2f90-691a-4c16-918f-a5b44dd38837%26entityType%3Dcollection%26workspaceId%3Debcdedd2-fbc8-46bc-95f1-bfb7d7b18460)

## Goals:
* [x] Build highly scalable RESTful API to create, read, update and delete data from a mongodb database.
* [x] Implement validation for endpoints to ensure that the data being entered is valid.
* [x] Implement pagination, sorting and filtering for get endpoints.
* [x] Use docker to build API containers.
* [x] Use kubernetes to deploy and manage containerized APIs.
* [ ] Use nginx as ingress controller to expose APIs to the internet.
* [ ] Implement horizontal pod autoscalling.
* [ ] Use prometheus and grafana to monitor the performance and health of APIs.
* [ ] Use kubernetes secrets to securely store the sensitive information.
