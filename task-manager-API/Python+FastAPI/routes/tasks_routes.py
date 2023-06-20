from fastapi import APIRouter
from fastapi import FastAPI, Body, HTTPException, status
from models.task import Task
from config.db import db
from typing import  List
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response, JSONResponse

tasks_routs= APIRouter()

@tasks_routs.get('/api/v1/tasks',  response_description="List all tasks", response_model=List[Task])
async def get_all_tasks():
    tasks= await db["tasks"].find().to_list(1000)
    return tasks

@tasks_routs.post("/api/v1/tasks", response_description="Add new task", response_model=Task)
async def create_student(task: Task = Body(...)):
    task = jsonable_encoder(task)
    new_task = await db["tasks"].insert_one(task)
    created_task = await db["tasks"].find_one({"_id": new_task.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_task)



@tasks_routs.get("/api/v1/tasks/{id}", response_description="Get a single task", response_model=Task)
async def show_single_task(id: str):
    task= await db["tasks"].find_one({"_id": id})
    if task is not None:
        return task

    raise HTTPException(status_code=404, detail=f"task {id} not found")



@tasks_routs.patch("/api/v1/tasks/{id}", response_description="Update a task", response_model=Task)
async def update_student(id: str, task: Task = Body(...)):
    task = {k: v for k, v in task.dict().items() if v is not None}

    if len(task) >= 1:
        update_result = await db["tasks"].update_one({"_id": id}, {"$set": task})

        if update_result.modified_count == 1:
            if (
                updated_task := await db["tasks"].find_one({"_id": id})
            ) is not None:
                return updated_task

    if (existing_task := await db["tasks"].find_one({"_id": id})) is not None:
        return existing_task

    raise HTTPException(status_code=404, detail=f"task {id} not found")


@tasks_routs.delete("/api/v1/tasks/{id}", response_description="Delete a task")
async def delete_task(id: str):
    delete_result = await db["tasks"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"task {id} not found")