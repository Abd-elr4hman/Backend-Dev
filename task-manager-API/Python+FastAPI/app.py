from fastapi import FastAPI
from bson import ObjectId
from models.task import Task
from routes.tasks_routes import tasks_routs



app= FastAPI()

app.include_router(tasks_routs)

